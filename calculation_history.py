#!/usr/bin/env python


# Calculation_history.py

def display_history(history):
    if not history:
        return "Calculation history is empty."

    result = "Calculation History:\n"
    for i, calc in enumerate(history, start=1):
        result += f"{i}. {calc['operation']} {calc['input_values'][0]} {calc['input_values'][1]} = {calc['result']}\n"

    return result
