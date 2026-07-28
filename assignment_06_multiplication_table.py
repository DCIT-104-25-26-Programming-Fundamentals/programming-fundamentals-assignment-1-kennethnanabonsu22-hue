# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 6
# Topic: Loops and Functions
# =============================================================================
#
# TASK: Multiplication Table Generator
#
# Write a Python program that generates multiplication tables using loops
# and functions.
#
# -----------------------------------------------------------------------------
# PART A — Single Table
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Print the multiplication table for that number from 1 to 12.
#
# Expected output (if user enters 5):
#
#   Multiplication Table for 5:
#   5  x  1  =  5
#   5  x  2  =  10
#   5  x  3  =  15
#   ...
#   5  x  12 =  60
#
# -----------------------------------------------------------------------------
# PART B — Bonus: Tables from 1 to N
# -----------------------------------------------------------------------------
# - Ask the user to enter a number N.
# - Print the full multiplication table for every number from 1 to N.
# - Add a separator line (e.g. "---") between each table.
#
# Expected output (if user enters 3):
#
#   Multiplication Table for 1:
#   1  x  1  =  1
#   ...
#   1  x  12 =  12
#   ---------------------------
#   Multiplication Table for 2:
#   2  x  1  =  2
#   ...
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - N must be a positive integer. If the user enters an invalid value,
#   print an error message and stop.
# - Each part must be in its own function (see scaffold below).
# - Complete Part A before attempting Part B.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 6
# Topic: Loops and Functions
# =============================================================================

def print_single_table(number: int) -> None:
    """Prints the multiplication table for a single number from 1 to 12."""
    print(f"Multiplication Table for {number}:")
    for i in range(1, 13):
        # We use {i:<2} to left-align the multiplier in a 2-character space.
        # This ensures the '=' signs line up perfectly for 1-9 and 10-12.
        print(f"{number}  x  {i:<2} =  {number * i}")

def print_tables_up_to_n(n: int) -> None:
    """Prints the multiplication tables for every number from 1 to n."""
    for i in range(1, n + 1):
        print_single_table(i)
        # Print the separator line between tables, but not after the very last one
        if i < n:
            print("-" * 27)

def get_positive_integer(prompt: str):
    """
    Helper function to handle input validation.
    Returns the integer if valid, or None if the user enters an invalid value.
    """
    try:
        val = int(input(prompt))
        if val <= 0:
            print("Error: Please enter a positive integer greater than 0.")
            return None
        return val
    except ValueError:
        print("Error: Invalid input. Please enter a whole number.")
        return None

def main():
    # -----------------------------------------------------------------------------
    # PART A — Single Table
    # -----------------------------------------------------------------------------
    print("=" * 45)
    print("PART A — Single Table")
    print("=" * 45)
    
    num_a = get_positive_integer("Enter a number: ")
    if num_a is None:
        return  # Stop the program if the input was invalid
        
    print()
    print_single_table(num_a)
    
    # -----------------------------------------------------------------------------
    # PART B — Bonus: Tables from 1 to N
    # -----------------------------------------------------------------------------
    print("\n" + "=" * 45)
    print("PART B — Bonus: Tables from 1 to N")
    print("=" * 45)
    
    n = get_positive_integer("Enter a number N: ")
    if n is None:
        return  # Stop the program if the input was invalid
        
    print()
    print_tables_up_to_n(n)

if __name__ == "__main__":
    main()
