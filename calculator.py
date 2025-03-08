# calculator.py

from sympy import sympify

def basic_calculator(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a / b if b != 0 else "Error: Division by zero!"
    else:
        return "Invalid operator"

def advanced_calculator(expression):
    """Evaluates advanced mathematical expressions safely."""
    try:
        result = sympify(expression)  # Evaluates the expression
        return result
    except Exception as e:
        return f"Error: {e}"
