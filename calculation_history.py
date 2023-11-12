#!/usr/bin/env python

# Function to display the calculation history
def display_history(history):
    """
    Displays the calculation history in a formatted way.
    """
    # Checks if the history is empty
    if not history:
        return "Calculation history is empty."

    # Builds the formatted history string
    result = "Calculation History:\n"
    for i, calc in enumerate(history, start=1):
        result += f"{i}. {calc['operation']} {calc['input_values'][0]} {calc['input_values'][1]} = {calc['result']}\n"

    return result
