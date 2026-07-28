# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 1
# Topic: Conditional Logic, Loops, and Functions
# =============================================================================
#
# TASK: Prime Number Checker
#
# Write a Python program that checks whether a given number is prime.
#
# A prime number is a whole number greater than 1 that has no divisors
# other than 1 and itself (e.g., 2, 3, 5, 7, 11, 13 ...).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLES
# -----------------------------------------------------------------------------
#
#   Enter a number: 7
#   7 is a prime number.
#
#   Enter a number: 10
#   10 is NOT a prime number.
#
#   Enter a number: 1
#   1 is NOT a prime number.
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement the logic inside a function (see scaffold below).
# - Numbers less than 2 are NOT prime — handle this inside the function.
# - The main block must call the function and print the result.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
def is_prime(number):
    """
    Checks if a given number is prime.
    Returns True if prime, False otherwise.
    """
    # Numbers less than 2 are not prime
    if number < 2:
        return False
    
    # Check for factors from 2 up to the square root of the number
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False  # Found a divisor, so it's not prime
            
    return True  # No divisors found, it is prime

def main():
    # Get input from the user
    user_input = input("Enter a number: ")
    
    try:
        num = int(user_input)
        
        # Call the function and print the result based on the return value
        if is_prime(num):
            print(f"{num} is a prime number.")
        else:
            print(f"{num} is NOT a prime number.")
            
    except ValueError:
        print("Invalid input. Please enter a whole number.")

# This ensures the main() function runs when the script is executed directly
if __name__ == "__main__":
    main()
