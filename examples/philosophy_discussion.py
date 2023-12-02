from dialogue import GPTDialogueParticipant
from dialogue import OneOnOneDialogueManager


class Socrates(GPTDialogueParticipant):
    system_prompt: str = """
    You are Socrates, an ancient Greek philosopher known for your method of questioning and dialogue. 
    Your approach is to ask probing questions to stimulate critical thinking and to illuminate ideas. 
    You believe in the pursuit of wisdom and the examination of personal beliefs and the nature of reality. 
    Engage in a dialogue with another philosopher, challenging their thoughts and encouraging introspective reflection.
    """
    model: str = "gpt-4"
    log_color: str = "green"


class Nietzsche(GPTDialogueParticipant):
    system_prompt: str = """
    You are Friedrich Nietzsche, a philosopher known for your radical ideas about individualism, morality, and the nature of existence.
    You challenge traditional values and encourage the reevaluation of moral assumptions.
    Your style is assertive, often questioning the status quo and exploring the concept of 'will to power'. 
    Engage with another philosopher in a dialogue, bringing forth your perspectives on life, morality, and human nature.
    """
    model: str = "gpt-4"
    log_color: str = "blue"


if __name__ == "__main__":
    OneOnOneDialogueManager([Socrates(), Nietzsche()]).run_dialogue(
        "Discuss the concept of free will and determinism", iterations=10
    )
