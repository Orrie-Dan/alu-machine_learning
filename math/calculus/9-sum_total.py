#!/usr/bin/env python3

def summation_i_squared(n):
    # Validate input
    if not isinstance(n, int) or n < 1:
        return None
    # Base case
    if n == 1:
        return 1
    # Recursive case
    return n**2 + summation_i_squared(n-1)

