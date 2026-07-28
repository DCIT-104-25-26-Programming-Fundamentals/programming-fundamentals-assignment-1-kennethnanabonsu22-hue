# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def read_matrix(rows, cols):
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


def print_matrix(matrix):
    """Displays a matrix in a neat, column-aligned grid."""
    if not matrix:
        print("(empty)")
        return
    # Find the maximum width needed for each column
    num_cols = len(matrix[0])
    widths = [0] * num_cols
    for row in matrix:
        for j, val in enumerate(row):
            widths[j] = max(widths[j], len(str(val)))
    # Print each row with right-aligned values
    for row in matrix:
        line = "  ".join(f"{val:>{widths[j]}}" for j, val in enumerate(row))
        print(line)


# =============================================================================
# PART A — Transpose a Matrix
# =============================================================================

def transpose_matrix(matrix):
    """Returns the transpose of the given matrix (rows <-> columns)."""
    if not matrix:
        return []
    rows = len(matrix)
    cols = len(matrix[0])
    result = []
    for i in range(cols):
        new_row = []
        for j in range(rows):
            new_row.append(matrix[j][i])
        result.append(new_row)
    return result


# =============================================================================
# PART B — Add Two Matrices
# =============================================================================

def add_matrices(mat1, mat2):
    """Returns the element-wise sum of two matrices of the same size."""
    rows = len(mat1)
    cols = len(mat1[0])
    result = []
    for i in range(rows):
        new_row = []
        for j in range(cols):
            new_row.append(mat1[i][j] + mat2[i][j])
        result.append(new_row)
    return result


# =============================================================================
# PART C — Multiply Two Matrices
# =============================================================================

def multiply_matrices(mat_a, mat_b):
    """Returns the product A x B. Requires cols(A) == rows(B)."""
    rows_a = len(mat_a)
    cols_a = len(mat_a[0])
    cols_b = len(mat_b[0])
    result = []
    for i in range(rows_a):
        new_row = []
        for j in range(cols_b):
            total = 0
            for k in range(cols_a):
                total += mat_a[i][k] * mat_b[k][j]
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
    rows_a = int(input("Enter number of rows: "))
    cols_a = int(input("Enter number of columns: "))
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
    rows_b = int(input("Enter number of rows: "))
    cols_b = int(input("Enter number of columns: "))

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
    rows_c = int(input("Enter number of rows for matrix A (M): "))
    cols_a_c = int(input("Enter number of columns for matrix A (N): "))

    print("Enter matrix A:")
    mat_c1 = read_matrix(rows_c, cols_a_c)

    # B must have N rows; user only chooses P (columns of B)
    rows_b_c = cols_a_c  # required for multiplication to be valid
    cols_b_c = int(input(f"Enter number of columns for matrix B (P): "))

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
