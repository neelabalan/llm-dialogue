import abc
import datetime
import logging
import os
import typing

import openai
import typing_extensions
from rich.logging import RichHandler

logging.basicConfig(
    level="INFO",
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler()],
)


logger = logging.getLogger(__name__)


class DialogueParticipant(abc.ABC):
    system_prompt: str
    model: str

    @abc.abstractmethod
    def dispatch(self, message: str) -> str:
        pass


class GPTDialogueParticipant(DialogueParticipant):
    model: typing.Literal["gpt-3.5", "gpt-4"]
    log_color: typing.Literal["green", "blue", "red", "yellow"] = "green"
    _client = openai.OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

    def dispatch(self, message: str) -> str:
        response = self._client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": message},
            ],
        )
        text = response.choices[0].message.content
        logger.info(
            f"[{self.log_color}]From {type(self).__name__}: {text}\n\n[/{self.log_color}]",
            extra={"markup": True},
        )
        return text


class OneOnOneDialogueManager:
    def __init__(self, partcipants: typing.List[DialogueParticipant]):
        self.participants = partcipants
        self.memory = []
        self._check_participant_count()

    def swap_participant(
        self, participant: DialogueParticipant, replace_with: DialogueParticipant
    ) -> typing_extensions.Self:
        self.participants.remove(participant)
        self.participants.append(replace_with)
        return self

    def _check_participant_count(self):
        if not len(self.participants) == 2:
            raise ValueError(
                "One on one dialogue manager can only handle 2 participants."
            )

    def run_dialogue(self, initial_prompt: str, iterations: int = 5):
        # Logic to control the flow of the dialogue
        response = initial_prompt
        for i in range(iterations):
            current_participant = self.participants[i % 2]
            response = current_participant.dispatch(response)
            self.memory.append(
                {
                    "timestamp": datetime.datetime.now(),
                    "participant": type(current_participant).__name__,
                    "response": response,
                }
            )
