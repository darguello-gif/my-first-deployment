"""
Simple Calculator App
This is your first app that will be deployed with automated testing!
"""

def add(a, b):
    """Add two numbers together"""
    return a + b

def subtract(a, b):
    """Subtract b from a"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide a by b"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power(base, exponent):
    """Raise base to the power of exponent"""
    return base ** exponent

def greet(name):
    """Greet a user by name"""
    if not name:
        return "Hello, stranger!"
    return f"Hello, {name}!"

# This runs when you execute the file directly
if __name__ == "__main__":
    print("🧮 Calculator App")
    print("=" * 40)
    print(f"5 + 3 = {add(5, 3)}")
    print(f"10 - 4 = {subtract(10, 4)}")
    print(f"6 * 7 = {multiply(6, 7)}")
    print(f"20 / 4 = {divide(20, 4)}")
    print(f"2 ^ 3 = {power(2, 3)}")
    print()
    print(greet("Diego"))
