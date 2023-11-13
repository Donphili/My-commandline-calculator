#!/usr/bin/env python

# Addition
def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

# Subtraction
def subtract(a, b):
    """Returns the result of subtracting b from a."""
    return a - b                                           

# Multiplication
def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b

# Division
def divide(a, b):
    """Returns the result of dividing a by b. 
    If b is zero, returns an error message."""
    if b == 0:
        return "Cannot divide by zero"
    return a / b
