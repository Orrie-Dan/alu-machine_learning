#!/usr/bin/env python3
"""Module for matrix transpose"""


def matrix_transpose(matrix):
    """
    Returns the transpose of a 2D matrix

    Args:
        matrix: A 2D list representing a matrix

    Returns:
        A new matrix that is the transpose of the input matrix
    """
    rows = len(matrix)
    cols = len(matrix[0])
    transpose = [[matrix[row][col] for row in range(rows)]
                 for col in range(cols)]
    return transpose
