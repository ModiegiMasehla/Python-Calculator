"""
Beginner-friendly calculator.

This module contains the calculation logic and a simple command-line interface.
It uses only Python's standard library.
"""

import math


def calculate(first_number, operator, second_number=None):
    """Perform one supported calculation and return the result."""
    if operator == "+":
        if second_number is None:
            raise ValueError("Addition needs two numbers.")
        return first_number + second_number

    if operator == "-":
        if second_number is None:
            raise ValueError("Subtraction needs two numbers.")
        return first_number - second_number

    if operator == "*":
        if second_number is None:
            raise ValueError("Multiplication needs two numbers.")
        return first_number * second_number

    if operator == "/":
        if second_number is None:
            raise ValueError("Division needs two numbers.")
        if second_number == 0:
            raise ZeroDivisionError("You cannot divide by zero.")
        return first_number / second_number

    if operator == "%":
        if second_number is None:
            raise ValueError("Percentage needs two numbers.")
        # For example, 20 % 50 means 20 percent of 50 = 10.
        return first_number / 100 * second_number

    if operator == "^":
        if second_number is None:
            raise ValueError("Powers need two numbers.")
        result = first_number ** second_number
        if isinstance(result, complex):
            raise ValueError("This calculator does not support complex results.")
        return result

    if operator == "sqrt":
        if first_number < 0:
            raise ValueError("Square root is not defined for negative numbers here.")
        return math.sqrt(first_number)

    if operator == "square":
        return first_number ** 2

    if operator == "reciprocal":
        if first_number == 0:
            raise ZeroDivisionError("Zero has no reciprocal.")
        return 1 / first_number

    raise ValueError(f"Unsupported operator: {operator}")


def format_result(number):
    """Display whole-number results without a trailing .0."""
    if isinstance(number, float) and math.isfinite(number) and number.is_integer():
        return str(int(number))
    return str(number)


def run_calculator():
    """Run the interactive command-line calculator."""
    print("=== Beginner Python Calculator ===")
    print("Operations: +  -  *  /  %  ^  sqrt  square  reciprocal")
    print("For a one-number operation, enter sqrt, square, or reciprocal.")
    print("Type q at any prompt to quit.\n")

    while True:
        first_text = input("Enter the first number: ").strip()
        if first_text.lower() == "q":
            print("Till next time. Byyye!")
            break

        try:
            first_number = float(first_text)
        except ValueError:
            print("Please enter a valid number.\n")
            continue

        operator = input("Enter an operation: ").strip().lower()
        if operator == "q":
            print("Goodbye!")
            break

        if operator in {"sqrt", "square", "reciprocal"}:
            try:
                result = calculate(first_number, operator)
                print("Result:", format_result(result), "\n")
            except (ValueError, ZeroDivisionError, OverflowError) as error:
                print("Error:", error, "\n")
            continue

        if operator not in {"+", "-", "*", "/", "%", "^"}:
            print("Unsupported operation. Please choose one listed above.\n")
            continue

        second_text = input("Enter the second number: ").strip()
        if second_text.lower() == "q":
            print("Goodbye!")
            break

        try:
            second_number = float(second_text)
            result = calculate(first_number, operator, second_number)
            print("Result:", format_result(result), "\n")
        except (ValueError, ZeroDivisionError, OverflowError) as error:
            print("Error:", error, "\n")


if __name__ == "__main__":
    run_calculator()
