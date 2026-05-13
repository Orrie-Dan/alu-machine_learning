#!/usr/bin/env python3
"""Module for matrix multiplication"""


def mat_mul(mat1, mat2):
    """
    Performs matrix multiplication

    Args:
        mat1: First 2D matrix (list of lists) containing ints/floats
        mat2: Second 2D matrix (list of lists) containing ints/floats

    Returns:
        A new matrix that is the product of mat1 and mat2, or None if
        matrices cannot be multiplied
    """
    if len(mat1[0]) != len(mat2):
        return None

    rows1 = len(mat1)
    cols1 = len(mat1[0])
    cols2 = len(mat2[0])

    result = [[sum(mat1[i][k] * mat2[k][j] for k in range(cols1))
               for j in range(cols2)]
              for i in range(rows1)]

    return result
