#!/usr/bin/env python3

def poly_integral(poly, C=0):
    # Validate input
    if not isinstance(poly, list) or not all(isinstance(c, (int, float)) for c in poly):
        return None
    if not isinstance(C, (int, float)):
        return None
    
    # Start with the integration constant
    integral = [C]
    
    # Integrate each coefficient
    for i, coeff in enumerate(poly):
        new_coeff = coeff / (i + 1)
        # Represent as integer if it is whole number
        if new_coeff == int(new_coeff):
            new_coeff = int(new_coeff)
        integral.append(new_coeff)
    
    # Remove trailing zeros to make the list as small as possible
    while len(integral) > 1 and integral[-1] == 0:
        integral.pop()
    
    return integral

