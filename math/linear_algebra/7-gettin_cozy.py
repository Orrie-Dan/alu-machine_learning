#!/usr/bin/env python3
"""Module for concatenating 2D matrices along a specific axis"""


def cat_matrices2D(mat1, mat2, axis=0):
    """
    Concatenates two matrices along a specific axis

    Args:
        mat1: First 2D matrix (list of lists) containing ints/floats
        mat2: Second 2D matrix (list of lists) containing ints/floats
        axis: 0 for row-wise concatenation, 1 for column-wise concatenation

    Returns:
        A new matrix, or None if matrices cannot be concatenated
    """
    if axis == 0:
        if len(mat1[0]) != len(mat2[0]):
            return None
        return [row[:] for row in mat1] + [row[:] for row in mat2]
    elif axis == 1:
        if len(mat1) != len(mat2):
            return None
        return [mat1[i][:] + mat2[i][:] for i in range(len(mat1))]
    return None
