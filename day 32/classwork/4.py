"""https://www.codewars.com/kata/583f158ea20cfcbeb400000a/train/python"""

def arithmetic(a, b, operator):
    if operator == "add":
        return a + b
    elif operator == "subtract":
        return a - b
    elif operator == "multiply":
        return a * b
    elif operator == "divide":
        return a / (b * 1.0)