#!/usr/bin/env python3

def poly_derivative(poly):
    # Validate input
    if not isinstance(poly, list) or not all(isinstance(c, (int, float)) for c in poly):
        return None
    
    # Derivative calculation
    derivative = [i * poly[i] for i in range(1, len(poly))]
    
    # If derivative is empty (original poly was constant), return [0]
    return derivative if derivative else [0]

