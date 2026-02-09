#!/usr/bin/env python3
"""Module that computes the inverse of a matrix"""


def determinant(matrix):
    """Compute determinant of a square matrix"""

    n = len(matrix)

    if matrix == [[]]:
        return 1

    if n == 1:
        return matrix[0][0]

    if n == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]

    det = 0
    for col in range(n):
        sub = [
            [matrix[i][j] for j in range(n) if j != col]
            for i in range(1, n)
        ]
        det += ((-1) ** col) * matrix[0][col] * determinant(sub)

    return det


def cofactor(matrix):
    """Compute cofactor matrix"""

    n = len(matrix)

    if n == 1:
        return [[1]]

    cof = []
    for i in range(n):
        row = []
        for j in range(n):
            sub = [
                [matrix[r][c] for c in range(n) if c != j]
                for r in range(n) if r != i
            ]
            row.append(((-1) ** (i + j)) * determinant(sub))
        cof.append(row)

    return cof


def adjugate(matrix):
    """Compute adjugate matrix"""

    n = len(matrix)

    if n == 1:
        return [[1]]

    cof = cofactor(matrix)
    return [[cof[j][i] for j in range(n)] for i in range(n)]


def inverse(matrix):
    """Calculate the inverse of a matrix"""

    # Validation
    if (not isinstance(matrix, list) or len(matrix) == 0 or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a list of lists")

    n = len(matrix)

    if any(len(row) != n for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    # determinant
    det = determinant(matrix)

    # singular matrix
    if det == 0:
        return None

    # adjugate
    adj = adjugate(matrix)

    # divide by determinant
    inv = [[adj[i][j] / det for j in range(n)] for i in range(n)]

    return inv

