# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 5
# Topic: Loops, Sequences, and Functions
# =============================================================================
#
# TASK: Fibonacci Sequence Generator
#
# The Fibonacci sequence is a series of numbers where each number is the sum
# of the two numbers before it:
#
#   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#
# Write a Python program with TWO parts, each implemented as a function.
#
# -----------------------------------------------------------------------------
# PART A — Print the First N Terms
# -----------------------------------------------------------------------------
# - Ask the user how many terms (N) to display.
# - Print the first N numbers of the Fibonacci sequence on one line.
#
# Example:
#   How many terms? 7
#   Fibonacci sequence: 0 1 1 2 3 5 8
#
# -----------------------------------------------------------------------------
# PART B — Check if a Number Belongs to the Sequence
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Determine whether that number is a Fibonacci number.
# - Print an appropriate message.
#
# Example:
#   Enter a number to check: 13
#   13 is a Fibonacci number.
#
#   Enter a number to check: 20
#   20 is NOT a Fibonacci number.
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use a loop (not recursion) to generate the sequence in both parts.
# - N must be a positive integer. If it is not, print an error message.
# - Each part must be implemented in its own function (see scaffold below).
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
from typing import List

# Define a type alias for better readability
Matrix = List[List[int]]

# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def read_positive_int(prompt: str) -> int:
    """Prompts the user until they enter a valid positive integer."""
    while True:
        try:
            val = int(input(prompt))
            if val > 0:
                return val
            print("  -> Please enter a positive integer greater than 0.")
        except ValueError:
            print("  -> Invalid input. Please enter an integer.")

def read_matrix(rows: int, cols: int) -> Matrix:
    """Reads a matrix from the user, row by row."""
    matrix = []
    for i in range(rows):
        while True:
            row_input = input(f"Enter row {i + 1}: ").split()
            if len(row_input) == cols:
                try:
                    row = [int(x) for x in row_input]
                    matrix.append(row)
                    break
                except ValueError:
                    print("  -> Please enter integers only.")
            else:
                print(f"  -> Expected {cols} values, got {len(row_input)}. Try again.")
    return matrix

def print_matrix(matrix: Matrix) -> None:
    """Displays a matrix in a neat, column-aligned grid."""
    if not matrix:
        print("(empty)")
        return
    
    num_cols = len(matrix[0])
    widths = [0] * num_cols
    for row in matrix:
        for j, val in enumerate(row):
            widths[j] = max(widths[j], len(str(val)))
            
    for row in matrix:
        line = "  ".join(f"{val:>{widths[j]}}" for j, val in enumerate(row))
        print(line)

# =============================================================================
# PART A — Transpose a Matrix
# =============================================================================

def transpose_matrix(matrix: Matrix) -> Matrix:
    """Returns the transpose of the given matrix (rows <-> columns)."""
    if not matrix:
        return []
    rows = len(matrix)
    cols = len(matrix[0])
    return [[matrix[j][i] for j in range(rows)] for i in range(cols)]

# =============================================================================
# PART B — Add Two Matrices
# =============================================================================

def add_matrices(mat1: Matrix, mat2: Matrix) -> Matrix:
    """Returns the element-wise sum of two matrices of the same size."""
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        raise ValueError("Matrices must have the same dimensions to be added.")
        
    rows = len(mat1)
    cols = len(mat1[0])
    return [[mat1[i][j] + mat2[i][j] for j in range(cols)] for i in range(rows)]

# =============================================================================
# PART C — Multiply Two Matrices
# =============================================================================

def multiply_matrices(mat_a: Matrix, mat_b: Matrix) -> Matrix:
    """Returns the product A x B. Requires cols(A) == rows(B)."""
    cols_a = len(mat_a[0])
    rows_b = len(mat_b)
    
    if cols_a != rows_b:
        raise ValueError(f"Cannot multiply: Columns of A ({cols_a}) must match Rows of B ({rows_b}).")

    rows_a = len(mat_a)
    cols_b = len(mat_b[0])
    
    result = []
    for i in range(rows_a):
        new_row = []
        for j in range(cols_b):
            total = sum(mat_a[i][k] * mat_b[k][j] for k in range(cols_a))
            new_row.append(total)
        result.append(new_row)
    return result

# =============================================================================
# MAIN PROGRAM
# =============================================================================

def main():
    # ---------- PART A ----------
    print("=" * 60)
    print("PART A: Transpose a Matrix")
    print("=" * 60)
    rows_a = read_positive_int("Enter number of rows: ")
    cols_a = read_positive_int("Enter number of columns: ")
    print("Enter the matrix:")
    matrix_a = read_matrix(rows_a, cols_a)

    print("\nOriginal Matrix:")
    print_matrix(matrix_a)

    transposed = transpose_matrix(matrix_a)
    print("\nTransposed Matrix:")
    print_matrix(transposed)

    # ---------- PART B ----------
    print("\n" + "=" * 60)
    print("PART B: Add Two Matrices (same size)")
    print("=" * 60)
    rows_b = read_positive_int("Enter number of rows: ")
    cols_b = read_positive_int("Enter number of columns: ")

    print("Enter the FIRST matrix:")
    mat_b1 = read_matrix(rows_b, cols_b)
    print("Enter the SECOND matrix:")
    mat_b2 = read_matrix(rows_b, cols_b)

    print("\nFirst Matrix:")
    print_matrix(mat_b1)
    print("\nSecond Matrix:")
    print_matrix(mat_b2)

    sum_matrix = add_matrices(mat_b1, mat_b2)
    print("\nSum:")
    print_matrix(sum_matrix)

    # ---------- PART C ----------
    print("\n" + "=" * 60)
    print("PART C: Multiply Two Matrices (A is MxN, B is NxP)")
    print("=" * 60)
    rows_c = read_positive_int("Enter number of rows for matrix A (M): ")
    cols_a_c = read_positive_int("Enter number of columns for matrix A (N): ")

    print("Enter matrix A:")
    mat_c1 = read_matrix(rows_c, cols_a_c)

    rows_b_c = cols_a_c  # required for multiplication to be valid
    cols_b_c = read_positive_int(f"Enter number of columns for matrix B (P): ")

    print(f"Enter matrix B ({rows_b_c} rows, {cols_b_c} columns):")
    mat_c2 = read_matrix(rows_b_c, cols_b_c)

    print("\nMatrix A:")
    print_matrix(mat_c1)
    print("\nMatrix B:")
    print_matrix(mat_c2)

    product = multiply_matrices(mat_c1, mat_c2)
    print("\nProduct A x B:")
    print_matrix(product)

if __name__ == "__main__":
    main()
