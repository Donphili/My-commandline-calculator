#!/usr/bin/env python


# User_interaction.py

def handle_user_interaction(operations, calculation_history):
    while True:
        user_input = input("Enter your command (e.g., 'add 5 3', 'history', or 'exit'): ")
        input_list = user_input.split()

        if "exit" in input_list:
            print("Goodbye!")
            break

        if input_list[0] == "history":
            result = display_history(calculation_history)
            print(result)
            continue

        if len(input_list) < 3:
            print("Invalid input. Please use the format: <operation> <number1> <number2>")
        else:
            operation = input_list[0]
            num1 = float(input_list[1])
            num2 = float(input_list[2])

            if operation in operations:
                result = operations[operation](num1, num2)
                print(f"Result: {result}")

                calculation_data = {
                    'operation': operation,
                    'input_values': (num1, num2),
                    'result': result
                }

                calculation_history.append(calculation_data)
            else:
                print("Invalid operation. Supported operations: add, subtract, multiply, divide")

# Import the display_history function from calculation_history.py
from calculation_history import display_history
