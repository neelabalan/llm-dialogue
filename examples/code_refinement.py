from dialogue import GPTDialogueParticipant
from dialogue import OneOnOneDialogueManager


class CodeReviewer(GPTDialogueParticipant):
    system_prompt: str = """
    You are a highly intelligent code reviewer who will question and challenge the code people share with you. 
    You have very good reasoning capabilities and think outside of the box to question the aspects of the code such that it can be perfected.
    You are to talk to another GPT model to instruct it to refine the code further. Limit youself to verbal communication without sharing any code.
    """
    model: str = "gpt-4"
    log_color: str = "green"


class Programmer(GPTDialogueParticipant):
    system_prompt: str = "You are a python programmer who can write some good code. You'll take instructions from another GPT model to write code or improve your code."
    model: str = "gpt-4"
    log_color: str = "yellow"


if __name__ == "__main__":
    OneOnOneDialogueManager([Programmer(), CodeReviewer()]).run_dialogue(
        "Write a python code to find the sum of all numbers in a list", iterations=5
    )
