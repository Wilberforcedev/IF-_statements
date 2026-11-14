"""Command-line interface for the conditional statements learning lab."""

from __future__ import annotations

import argparse
import sys
from collections.abc import Callable
from typing import TextIO

from if_statements import __version__
from if_statements.lessons import LESSONS, Lesson
from if_statements.quiz import QUESTIONS, is_correct

Input = Callable[[str], str]


def _show_lesson(lesson: Lesson, output: TextIO) -> None:
    """Render one lesson in a readable console format."""

    print(f"\n{lesson.title}", file=output)
    print("-" * len(lesson.title), file=output)
    print(f"\n{lesson.summary}\n", file=output)
    print(lesson.example, file=output)
    print(f"\nKey idea: {lesson.takeaway}\n", file=output)


def _read_menu_choice(
    prompt: str,
    valid_choices: set[str],
    input_fn: Input,
    output: TextIO,
) -> str:
    """Read a menu choice, repeating until it is valid."""

    while True:
        try:
            choice = input_fn(prompt).strip().lower()
        except EOFError:
            print("\nInput ended. Goodbye.", file=output)
            return "q"
        if choice in valid_choices:
            return choice
        print(
            f"Please enter one of: {', '.join(sorted(valid_choices))}.",
            file=output,
        )


def _run_quiz(input_fn: Input, output: TextIO) -> None:
    """Ask all quiz questions and show explanations and the final score."""

    score = 0
    for number, question in enumerate(QUESTIONS, start=1):
        print(f"\n{number}. {question.prompt}", file=output)
        for index, choice in enumerate(question.choices, start=1):
            print(f"   {index}. {choice}", file=output)

        valid = {str(index) for index in range(1, len(question.choices) + 1)}
        valid.add("q")
        selection = _read_menu_choice(
            "Your answer (or q to return to the menu): ",
            valid,
            input_fn,
            output,
        )
        if selection == "q":
            return

        if is_correct(question, int(selection) - 1):
            score += 1
            print("Correct.", file=output)
        else:
            answer = question.choices[question.answer_index]
            print(f"Not quite. The answer is: {answer}.", file=output)
        print(question.explanation, file=output)

    print(f"\nYour score: {score}/{len(QUESTIONS)}", file=output)
    if score == len(QUESTIONS):
        print("Excellent work. You have mastered these basics.", file=output)
    elif score >= (len(QUESTIONS) + 1) // 2:
        print("Good progress. Review any topics that felt uncertain.", file=output)
    else:
        print("Review the lessons, then try the quiz again.", file=output)


def run(
    input_fn: Input = input,
    output: TextIO | None = None,
) -> int:
    """Run the interactive learning experience; return a process exit code."""

    output = output or sys.stdout
    print("Python If Statements Learning Lab", file=output)
    print("Learn conditional logic through short lessons and a quiz.", file=output)

    while True:
        print("\nMain menu", file=output)
        print("  1-5. Open a lesson", file=output)
        print("  q.   Quit", file=output)
        print("  quiz. Take the review quiz", file=output)
        valid = {str(index) for index in range(1, len(LESSONS) + 1)}
        valid.update({"q", "quiz"})
        choice = _read_menu_choice("Choose an option: ", valid, input_fn, output)

        if choice == "q":
            print("Goodbye. Keep practising!", file=output)
            return 0
        if choice == "quiz":
            _run_quiz(input_fn, output)
            continue
        _show_lesson(LESSONS[int(choice) - 1], output)


def main(argv: list[str] | None = None) -> int:
    """Parse command-line options and launch the learning lab."""

    parser = argparse.ArgumentParser(
        prog="if-lab",
        description="An interactive introduction to Python if statements.",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )
    parser.parse_args(argv)
    try:
        return run()
    except KeyboardInterrupt:
        print("\nInterrupted. Goodbye.", file=sys.stderr)
        return 130
