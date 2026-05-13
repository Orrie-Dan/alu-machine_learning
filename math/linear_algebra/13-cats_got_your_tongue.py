#!/usr/bin/env python3
"""Module for concatenating numpy arrays"""
import numpy as np


def np_cat(mat1, mat2, axis=0):
    """
    Concatenates two matrices along a specific axis

    Args:
        mat1: First numpy.ndarray
        mat2: Second numpy.ndarray
        axis: Axis along which to concatenate (0 for rows, 1 for columns)

    Returns:
        A new numpy.ndarray that is the concatenation of mat1 and mat2
    """
    return np.concatenate((mat1, mat2), axis=axis)
