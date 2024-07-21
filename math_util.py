def add(x, y):
    """Adds two numbers and returns the result."""
    return x + y

def subtract(x, y):
    """Subtracts two numbers and returns the result."""
    return x - y

def multiply(x, y):
    """Multiplies two numbers and returns the result."""
    return x * y

def divide(x, y):
    """Divides two numbers and returns the result.

    Raises ZeroDivisionError if the second number (y) is zero.
    """
    if y == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return x / y


