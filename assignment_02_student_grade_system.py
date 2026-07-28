# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 2
# Topic: Conditional Logic (if / elif / else) and Functions
# =============================================================================
#
# TASK: Student Grade System
#
# Write a Python program that reads a student's score and outputs the
# corresponding letter grade based on the scale below.
#
# Grading Scale:
#   Score 80 – 100  →  Grade A
#   Score 70 – 79   →  Grade B
#   Score 60 – 69   →  Grade C
#   Score 50 – 59   →  Grade D
#   Score below 50  →  Grade F
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLES
# -----------------------------------------------------------------------------
#
#   Enter student score (0-100): 85
#   Grade: A
#
#   Enter student score (0-100): 73
#   Grade: B
#
#   Enter student score (0-100): 45
#   Grade: F
#
#   Enter student score (0-100): 110
#   Error: Score must be between 0 and 100.
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST use functions (see scaffold below).
# - Validate that the score is within the range 0–100 inside get_grade().
#   If it is not, return None and let main() print the error message.
# - Use if / elif / else to determine the grade.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def get_grade(score):
    """
    Determines the letter grade based on the student's score.
    Returns None if the score is outside the valid 0-100 range.
    """
    # Validate the score range
    if score < 0 or score > 100:
        return None
    
    # Determine the grade using if/elif/else
    if score >= 80:
        return 'A'
    elif score >= 70:
        return 'B'
    elif score >= 60:
        return 'C'
    elif score >= 50:
        return 'D'
    else:
        return 'F'

def main():
    """
    Main function to handle user input, call get_grade(), and display the result.
    """
    try:
        # Get input from the user and convert to an integer
        user_input = input("Enter student score (0-100): ")
        score = int(user_input)
        
        # Call the function to get the grade
        grade = get_grade(score)
        
        # Check if the grade is None (invalid score) and print the corresponding message
        if grade is None:
            print("Error: Score must be between 0 and 100.")
        else:
            print(f"Grade: {grade}")
            
    except ValueError:
        # Handle cases where the user enters non-numeric input
        print("Error: Invalid input. Please enter a numeric score.")

# This ensures the main() function runs when the script is executed directly
if __name__ == "__main__":
    main()
