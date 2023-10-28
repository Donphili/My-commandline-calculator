#!/usr/bin/env python


# Imports necessary functions for mathematical operations
from math_functions import add, subtract, multiply, divide

# Create a loop for continuous user interaction
while True:
    # Retrieves user input
    user_input = input("Enter your command (e.g., 'add 5 3' or 'exit'): ")

    # Split the user input into a list of words
    input_list = user_input.split()

    # Check if the user wants to exit
    if "exit" in input_list:
        print("Goodbye!")
        break

    # Check if the user input is valid
    if len(input_list) < 3:
        print("Invalid input. Please use the format: <operation> <number1> <number2>")
    else:
        operation = input_list[0]
        num1 = float(input_list[1])
        num2 = float(input_list[2])

        # Perform the calculation based on the user's input
        if operation == "add":
            result = add(num1, num2)
        elif operation == "subtract":
            result = subtract(num1, num2)
        elif operation == "multiply":
            result = multiply(num1, num2)
        elif operation == "divide":
            result = divide(num1, num2)
        else:
            print("Invalid operation. Supported operations: add, subtract, multiply, divide")
            continue

        print(f"Result: {result}")
