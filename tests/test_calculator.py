"""Automated tests for the calculator's maths functions."""

import unittest

from calculator import calculate, format_result


class TestCalculator(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calculate(4, "+", 3), 7)

    def test_subtraction(self):
        self.assertEqual(calculate(4, "-", 7), -3)

    def test_multiplication(self):
        self.assertEqual(calculate(6, "*", 7), 42)

    def test_division(self):
        self.assertEqual(calculate(9, "/", 2), 4.5)

    def test_division_by_zero_raises_error(self):
        with self.assertRaises(ZeroDivisionError):
            calculate(5, "/", 0)

    def test_percentage_of_a_number(self):
        self.assertEqual(calculate(20, "%", 50), 10)

    def test_power(self):
        self.assertEqual(calculate(2, "^", 3), 8)

    def test_square_root(self):
        self.assertEqual(calculate(81, "sqrt"), 9)

    def test_square_root_of_negative_number_raises_error(self):
        with self.assertRaises(ValueError):
            calculate(-4, "sqrt")

    def test_square(self):
        self.assertEqual(calculate(5, "square"), 25)

    def test_reciprocal(self):
        self.assertEqual(calculate(4, "reciprocal"), 0.25)

    def test_reciprocal_of_zero_raises_error(self):
        with self.assertRaises(ZeroDivisionError):
            calculate(0, "reciprocal")

    def test_unknown_operation_raises_error(self):
        with self.assertRaises(ValueError):
            calculate(1, "???", 2)

    def test_missing_second_number_raises_error(self):
        with self.assertRaises(ValueError):
            calculate(1, "+")

    def test_format_whole_number(self):
        self.assertEqual(format_result(5.0), "5")

    def test_format_decimal(self):
        self.assertEqual(format_result(5.25), "5.25")


if __name__ == "__main__":
    unittest.main()
