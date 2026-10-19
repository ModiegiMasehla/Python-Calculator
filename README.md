# Beginner Python Calculator

A simple, beginner-friendly command-line calculator written in Python. It uses only Python's standard library, so there are no extra packages to install.

## Features

- Addition (`+`), subtraction (`-`), multiplication (`*`) and division (`/`)
- Percentage of a number (`%`): `20 % 50` means 20% of 50, which is 10
- Powers (`^`), square root (`sqrt`), square (`square`) and reciprocal (`reciprocal`)
- Handles invalid number input and unsupported operations
- Displays helpful errors for division by zero, square roots of negative numbers and reciprocal of zero
- Automated unit tests using Python's built-in `unittest`

## Requirements

- Python 3.8 or newer
- No third-party packages required

## Run the calculator

Open a terminal in the folder containing `calculator.py` and run:

```bash
python3 calculator.py
```

Example:

```text
Enter the first number: 12
Enter an operation: *
Enter the second number: 3
Result: 36
```

For one-number operations, enter the number and then `sqrt`, `square`, or `reciprocal`. Type `q` at a prompt to quit.

## Run the tests

From the project root, run:

```bash
python3 -m unittest discover -s tests -v
```

The tests check arithmetic, percentage calculations, powers, one-number operations, error handling and result formatting.

## Project structure

```text
python_beginner_calculator/
├── calculator.py
├── README.md
└── tests/
    └── test_calculator.py
```

## How the code works

- `calculate(...)` contains the maths logic and returns the answer.
- `format_result(...)` displays whole-number answers without unnecessary `.0`.
- `run_calculator()` asks the user for input, validates it, calls `calculate(...)`, and prints the result.
- `if __name__ == "__main__":` starts the interactive calculator only when this file is run directly. Importing it in tests does not start the prompt.

## Notes and limitations

- This is a command-line calculator, not a graphical app.
- Each calculation is entered separately; expression chains and parentheses are not implemented.
- Percentage is defined as “first number percent of second number.”
- Floating-point arithmetic can have tiny rounding differences for some decimal calculations.
