"""Quiz content and scoring helpers."""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Question:
    """A multiple-choice question with one zero-based correct answer."""

    prompt: str
    choices: tuple[str, ...]
    answer_index: int
    explanation: str


QUESTIONS: tuple[Question, ...] = (
    Question(
        prompt="Which keyword starts a conditional block in Python?",
        choices=("when", "if", "check", "then"),
        answer_index=1,
        explanation="Python uses ``if`` followed by a Boolean condition and a colon.",
    ),
    Question(
        prompt="What does ``else`` do?",
        choices=(
            "Repeats the condition",
            "Runs when the preceding conditions were false",
            "Ends the program",
            "Declares a variable",
        ),
        answer_index=1,
        explanation="The else block is the fallback when no earlier branch matched.",
    ),
    Question(
        prompt="Which branch is checked after an ``if`` condition is false?",
        choices=("otherwise", "elif", "except", "finally"),
        answer_index=1,
        explanation="``elif`` means 'else if' and checks another condition.",
    ),
    Question(
        prompt="What is the result of ``True and False``?",
        choices=("True", "False", "None", "An error"),
        answer_index=1,
        explanation="``and`` is true only when both operands are true.",
    ),
    Question(
        prompt="In an ``if``/``elif``/``else`` chain, how many branches run?",
        choices=(
            "Every branch whose condition is true",
            "At most one branch",
            "Exactly two branches",
            "No branch",
        ),
        answer_index=1,
        explanation=(
            "Python runs the first matching branch and skips the remaining "
            "branches in that chain."
        ),
    ),
)


def is_correct(question: Question, selection: int) -> bool:
    """Return whether a zero-based selection is the question's correct answer."""

    return selection == question.answer_index
