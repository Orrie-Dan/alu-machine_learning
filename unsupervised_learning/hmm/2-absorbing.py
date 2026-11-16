#!/usr/bin/env python3
'''
    function def absorbing(P): that
    determines if a markov chain is absorbing
'''


import numpy as np


def absorbing(P):
    '''
        Determines if a markov chain is absorbing

        P: square 2D numpy.ndarray of shape (n, n) representing
           the standard transition matrix
        Returns: True if it is absorbing, False otherwise,
                 or None on failure
    '''
    if type(P) is not np.ndarray or len(P.shape) != 2:
        return None
    n1, n2 = P.shape
    if n1 != n2 or n1 == 0:
        return None

    absorbed = np.diagonal(P) == 1
    if not absorbed.any():
        return False

    # Grow the set of states that can reach an absorbing state
    changed = True
    while changed:
        changed = False
        for i in range(n1):
            if not absorbed[i] and (P[i, absorbed] > 0).any():
                absorbed[i] = True
                changed = True

    return bool(absorbed.all())
