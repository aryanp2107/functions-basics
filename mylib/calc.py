"""
A calculator module that provides basic arithmetic operations.
This module includes functions for addition, subtraction, multiplication, and division.
"""


def add(a, b):
    """Return the sum of a and b."""
    return a + b


def sub(a, b):
    """Return the difference of a and b."""
    return a - b


def mul(a, b):
    """Return the product of a and b."""
    return a * b


def div(a, b):
    """Return the quotient of a and b. Raises ValueError if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def power(a, b):
    """Return a raised to the power of b."""
    return a**b


def modulus(a, b):
    """Return the modulus of a and b."""
    return a % b


def main():
    """Example usage of the calculator functions."""
    print("Addition:", add(5, 3))
    print("Subtraction:", sub(5, 3))
    print("Multiplication:", mul(5, 3))
    print("Division:", div(5, 3))
    print("Power:", power(5, 3))
    print("Modulus:", modulus(5, 3))
