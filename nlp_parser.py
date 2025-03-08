# nlp_parser.py

import spacy
from calculator import basic_calculator, advanced_calculator

# Load the English NLP model
nlp = spacy.load("en_core_web_sm")

def parse_input(text):
    doc = nlp(text)
    expression = ""

    # Extract numbers and operators from the input text
    for token in doc:
        if token.pos_ in ["NUM", "SYM"] or token.text in ["+", "-", "*", "/"]:
            expression += token.text + " "  # Build the full mathematical expression

    expression = expression.strip()  # Remove trailing spaces

    if expression:
        return advanced_calculator(expression)  # Use SymPy to evaluate expressions
    else:
        return "Invalid input. Please provide a valid expression."
