# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 9
# =============================================================================
#
# TASK: Console-Based Simple Calculator
#
# Build a calculator program that runs in the console and performs basic
# arithmetic operations based on the user's input.
#
# -----------------------------------------------------------------------------
# OPERATIONS YOUR CALCULATOR MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Addition          ( + )    e.g.  10 + 3  =  13
#   2. Subtraction       ( - )    e.g.  10 - 3  =  7
#   3. Multiplication    ( * )    e.g.  10 * 3  =  30
#   4. Division          ( / )    e.g.  10 / 3  =  3.33
#   5. Modulus           ( % )    e.g.  10 % 3  =  1  (remainder)
#   6. Exponentiation    ( ** )   e.g.  2 ** 8  =  256
#   7. Quit
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ============================
#        SIMPLE CALCULATOR
#   ============================
#   1. Addition
#   2. Subtraction
#   3. Multiplication
#   4. Division
#   5. Modulus
#   6. Exponentiation
#   7. Quit
#   Select an operation (1-7):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Select an operation (1-7): 4
#   Enter first number : 10
#   Enter second number: 3
#   Result: 10 / 3 = 3.33
#
#   Select an operation (1-7): 4
#   Enter first number : 5
#   Enter second number: 0
#   Error: Cannot divide by zero.
#
#   Select an operation (1-7): 7
#   Goodbye!
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Each arithmetic operation MUST be written as its own function.
# - Use a loop so the calculator keeps running until the user selects Quit.
# - Division by zero must be caught and handled with a clear error message
#   (do NOT let the program crash).
# - Division results should be rounded to 2 decimal places.
# - Handle invalid menu choices gracefully.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def add(a, b):
    """Return the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Return the difference of two numbers."""
    return a - b

def multiply(a, b):
    """Return the product of two numbers."""
    return a * b

def divide(a, b):
    """Return the quotient of two numbers, rounded to 2 decimal places."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return round(a / b, 2)

def modulus(a, b):
    """Return the remainder of dividing a by b."""
    if b == 0:
        raise ZeroDivisionError("Cannot perform modulus by zero.")
    return a % b

def exponent(a, b):
    """Return a raised to the power of b."""
    return a ** b

def get_number(prompt):
    """Prompt the user for a number and return it as a float."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    """Main function to run the simple calculator."""
    operations = {
        '1': ('+', 'Addition', add),
        '2': ('-', 'Subtraction', subtract),
        '3': ('*', 'Multiplication', multiply),
        '4': ('/', 'Division', divide),
        '5': ('%', 'Modulus', modulus),
        '6': ('**', 'Exponentiation', exponent),
    }

    while True:
        print("\n============================")
        print("     SIMPLE CALCULATOR")
        print("============================")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulus")
        print("6. Exponentiation")
        print("7. Quit")

        choice = input("Select an operation (1-7): ")

        if choice == '7':
            print("Goodbye!")
            break
        elif choice in operations:
            symbol, name, func = operations[choice]
            a = get_number("Enter first number : ")
            b = get_number("Enter second number: ")
            try:
                result = func(a, b)
                # Format operands nicely (show as int if whole number)
                a_str = int(a) if a.is_integer() else a
                b_str = int(b) if b.is_integer() else b
                # Format result nicely (show as int if whole number, else 2 decimals for division)
                if choice == '4':
                    result_str = f"{result:.2f}" if not result.is_integer() else int(result)
                else:
                    result_str = int(result) if isinstance(result, float) and result.is_integer() else result
                print(f"Result: {a_str} {symbol} {b_str} = {result_str}")
            except ZeroDivisionError as e:
                print(f"Error: {e}")
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
