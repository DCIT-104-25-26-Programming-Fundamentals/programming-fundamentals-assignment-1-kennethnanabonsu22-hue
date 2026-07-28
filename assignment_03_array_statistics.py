# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
def calculate_sum(numbers):
    """
    Calculates the sum of a list of numbers using a loop.
    """
    total = 0
    for num in numbers:
        total += num
    return total

def calculate_average(numbers):
    """
    Calculates the average of a list of numbers.
    """
    total = calculate_sum(numbers)
    return total / len(numbers)

def calculate_max(numbers):
    """
    Finds the maximum value in a list of numbers using a loop.
    """
    max_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val

def calculate_min(numbers):
    """
    Finds the minimum value in a list of numbers using a loop.
    """
    min_val = numbers[0]
    for num in numbers:
        if num < min_val:
            min_val = num
    return min_val

def format_number(value):
    """
    Formats a number to remove the trailing .0 if it is a whole number.
    """
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    return str(value)

def main():
    """
    Main function to handle user input, validate N, collect numbers, 
    and display the calculated statistics.
    """
    try:
        n = int(input("How many numbers? "))
    except ValueError:
        print("Error: Invalid input. Please enter an integer.")
        return

    # Validate that N is a positive integer
    if n <= 0:
        print("Error: N must be a positive integer.")
        return

    # Collect the numbers from the user
    numbers = []
    for i in range(1, n + 1):
        try:
            num = float(input(f"Enter number {i}: "))
            numbers.append(num)
        except ValueError:
            print("Error: Invalid number.")
            return

    # Calculate statistics using the custom functions
    total = calculate_sum(numbers)
    avg = calculate_average(numbers)
    max_val = calculate_max(numbers)
    min_val = calculate_min(numbers)

    # Print the results formatted to match the expected output
    print("\nResults:")
    print(f"{'Sum:':<9}{format_number(total)}")
    print(f"{'Average:':<9}{format_number(avg)}")
    print(f"{'Maximum:':<9}{format_number(max_val)}")
    print(f"{'Minimum:':<9}{format_number(min_val)}")

# This ensures the main() function runs when the script is executed directly
if __name__ == "__main__":
    main()
