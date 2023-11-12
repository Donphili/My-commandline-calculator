#!/usr/bin/env python

# Import the display_history function from calculation_history.py
from calculation_history import display_history

# Function to handle user interaction
def handle_user_interaction(operations, calculation_history):
    """
    Continuously interacts with the user, performs calculations, and maintains a history.
    """
    while True:
        # Retrieves user input
        user_input = input("Enter your command (e.g., 'add 5 3', 'history', or 'exit'): ")
        # Splits the user input into a list of words
        input_list = user_input.split()

        # Checks if the user wants to exit
        if "exit" in input_list:
            print("Goodbye!")
            break

        # Displays the calculation history
        if input_list[0] == "history":
            result = display_history(calculation_history)
            print(result)
            continue

        # Validates user input
        if len(input_list) < 3:
            print("Invalid input. Please use the format: <operation> <number1> <number2>")
        else:
            # Extracts operation and numbers from user input
            operation = input_list[0]
            num1 = float(input_list[1])
            num2 = float(input_list[2])

            # Performs the calculation based on the user's input
            if operation in operations:
                result = operations[operation](num1, num2)
                print(f"Result: {result}")

                # Records the calculation in the history
                calculation_data = {
                    'operation': operation,
                    'input_values': (num1, num2),
                    'result': result
                }

                calculation_history.append(calculation_data)
            else:
                print("Invalid operation. Supported operations: add, subtract, multiply, divide")

# This script assumes that 'operations' and 'calculation_history' are defined elsewhere.
# Make sure these variables are available or modify the script accordingly.
