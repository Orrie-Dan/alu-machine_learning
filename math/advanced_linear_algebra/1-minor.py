#!/usr/bin/env python3
"""Module that computes the minor matrix"""


def determinant(matrix):
    """Compute determinant of a square matrix"""

    n = len(matrix)

    # 0x0 matrix determinant
    if matrix == [[]]:
        return 1

    # 1x1
    if n == 1:
        return matrix[0][0]

    # 2x2
    if n == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]

    # recursive Laplace expansion
    det = 0
    for col in range(n):
        sub = [
            [matrix[i][j] for j in range(n) if j != col]
            for i in range(1, n)
        ]
        det += ((-1) ** col) * matrix[0][col] * determinant(sub)

    return det


def minor(matrix):
    """Calculate the minor matrix of a matrix"""

    # Validate list of lists
    if (not isinstance(matrix, list) or len(matrix) == 0 or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a list of lists")

    n = len(matrix)

    # Validate square
    if any(len(row) != n for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    # Special case 1x1
    if n == 1:
        return [[1]]

    # Compute minor matrix
    minor_matrix = []

    for i in range(n):
        row_minors = []
        for j in range(n):

            # build submatrix excluding row i and col j
            sub = [
                [matrix[r][c] for c in range(n) if c != j]
                for r in range(n) if r != i
            ]

            row_minors.append(determinant(sub))

        minor_matrix.append(row_minors)

    return minor_matrix

