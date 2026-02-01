#!/usr/bin/env python3
def determinant(matrix):
    """Calculates the determinant of a matrix"""

    # Validate matrix is a list of lists
    if not isinstance(matrix, list) or any(not isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    # Special case: 0x0 matrix
    if matrix == [[]]:
        return 1

    # Matrix must not be empty
    if len(matrix) == 0:
        raise TypeError("matrix must be a list of lists")

    # Validate square matrix
    n = len(matrix)
    for row in matrix:
        if len(row) != n:
            raise ValueError("matrix must be a square matrix")

    # Base case: 1x1 matrix
    if n == 1:
        return matrix[0][0]

    # Base case: 2x2 matrix
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    # Recursive expansion by first row
    det = 0
    for col in range(n):
        sub_matrix = [
            row[:col] + row[col + 1:]
            for row in matrix[1:]
        ]
        det += ((-1) ** col) * matrix[0][col] * determinant(sub_matrix)

    return det

