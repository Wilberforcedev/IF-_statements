"""Lesson content for Python's conditional statements."""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Lesson:
    """A short, self-contained teaching unit."""

    title: str
    summary: str
    example: str
    takeaway: str


LESSONS: tuple[Lesson, ...] = (
    Lesson(
        title="A simple if statement",
        summary=(
            "Use ``if`` to run an indented block only when a condition is true. "
            "A condition is an expression that evaluates to True or False."
        ),
        example='''temperature = 28

if temperature > 25:
    print("It is a warm day.")''',
        takeaway=(
            "The colon starts the block, and indentation shows which statements "
            "belong to it."
        ),
    ),
    Lesson(
        title="if and else",
        summary=(
            "Use ``else`` to provide a fallback block. Exactly one of the two "
            "branches runs."
        ),
        example='''balance = 12_000
price = 15_000

if balance >= price:
    print("Purchase approved")
else:
    print("Not enough funds")''',
        takeaway="The ``else`` branch has no condition of its own.",
    ),
    Lesson(
        title="if, elif, and else",
        summary=(
            "Use ``elif`` to check another condition when earlier conditions "
            "were false. Python stops at the first matching branch."
        ),
        example='''score = 76

if score >= 80:
    grade = "A"
elif score >= 70:
    grade = "B"
elif score >= 60:
    grade = "C"
else:
    grade = "Needs more practice"

print(grade)''',
        takeaway=(
            "Put more specific or higher-threshold checks first to avoid "
            "making a later branch unreachable."
        ),
    ),
    Lesson(
        title="Combining conditions",
        summary=(
            "Use ``and``, ``or``, and ``not`` to combine Boolean expressions. "
            "Parentheses can make the intended grouping easier to read."
        ),
        example='''age = 22
has_ticket = True

if age >= 18 and has_ticket:
    print("Entry allowed")
else:
    print("Entry denied")''',
        takeaway=(
            "Prefer clear comparisons and parentheses when a condition has "
            "several parts."
        ),
    ),
    Lesson(
        title="Nested conditions",
        summary=(
            "An ``if`` block can contain another ``if`` statement. Use nesting "
            "when the second decision only matters after the first succeeds."
        ),
        example='''is_registered = True
fee_paid = False

if is_registered:
    if fee_paid:
        print("You may sit the exam.")
    else:
        print("Please clear the fee first.")
else:
    print("Register before booking an exam.")''',
        takeaway=(
            "If nesting becomes deep, consider combining conditions or "
            "extracting a clearly named helper function."
        ),
    ),
)
