# Python If Statements Learning Lab

A small, interactive command-line course for learning Python conditional logic. It
includes five short lessons, runnable code examples, and a multiple-choice review
quiz with explanations. The app uses only the Python standard library.

> This project turns the repository's original topic, “If statements in JAVA,” into
> a Python learning resource, as requested.

## Requirements

- Python 3.10 or newer
- pip

## Install

From the repository root:

```bash
python -m venv .venv
```

Activate the environment:

```bash
# macOS / Linux
source .venv/bin/activate

# Windows PowerShell
.venv\Scripts\Activate.ps1
```

Then install the project:

```bash
python -m pip install .
```

## Run

Start the installed command:

```bash
if-lab
```

Or run directly from the source tree:

```bash
PYTHONPATH=src python -m if_statements
```

The menu opens lessons on `if`, `if/else`, `if/elif/else`, combined Boolean
conditions, and nested conditionals. Choose `quiz` to check your understanding or
`q` to exit. Use `if-lab --help` for command-line help and `if-lab --version`
to print the installed version.

## Development

Install the optional linting tools and run Ruff:

```bash
python -m pip install -e ".[dev]"
ruff check .
ruff format --check .
```

The GitHub Actions workflow checks formatting, lint, and package build on pushes
and pull requests.

## Project layout

```text
src/if_statements/
├── __init__.py
├── __main__.py
├── cli.py
├── lessons.py
└── quiz.py
```

## License

MIT. See [LICENSE](LICENSE).
