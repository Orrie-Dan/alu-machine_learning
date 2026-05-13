#!/usr/bin/env python3
"""Module that determines matrix definiteness"""

import numpy as np


def definiteness(matrix):
    """Calculate definiteness of a matrix"""

    # Type check
    if not isinstance(matrix, np.ndarray):
        raise TypeError("matrix must be a numpy.ndarray")

    # Must be 2D square and non-empty
    if matrix.ndim != 2 or matrix.shape[0] == 0 or matrix.shape[0] != matrix.shape[1]:
        return None

    # Must be symmetric
    if not np.allclose(matrix, matrix.T):
        return None

    # Eigenvalues
    eigvals = np.linalg.eigvals(matrix)

    # tolerance for floating error
    tol = 1e-8

    positive = np.all(eigvals > tol)
    non_negative = np.all(eigvals >= -tol)
    negative = np.all(eigvals < -tol)
    non_positive = np.all(eigvals <= tol)

    if positive:
        return "Positive definite"
    if non_negative:
        return "Positive semi-definite"
    if negative:
        return "Negative definite"
    if non_positive:
        return "Negative semi-definite"

    if np.any(eigvals > tol) and np.any(eigvals < -tol):
        return "Indefinite"

    return None
