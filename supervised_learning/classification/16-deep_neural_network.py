#!/usr/bin/env python3
"""
Deep Neural Network for binary classification
"""

import numpy as np


class DeepNeuralNetwork:
    """
    Defines a deep neural network performing binary classification
    """

    def __init__(self, nx, layers):
        # nx validation
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")

        # layers validation
        if not isinstance(layers, list) or len(layers) == 0:
            raise TypeError("layers must be a list of positive integers")

        if not all(isinstance(x, int) and x > 0 for x in layers):
            raise TypeError("layers must be a list of positive integers")

        self.nx = nx
        self.layers = layers

        self.L = len(layers)
        self.cache = {}
        self.weights = {}

        for l in range(1, self.L + 1):
            layer_size = layers[l - 1]

            if l == 1:
                prev = nx
            else:
                prev = layers[l - 2]

            # He initialization
            self.weights["W" + str(l)] = (
                np.random.randn(layer_size, prev) * np.sqrt(2 / prev)
            )
            self.weights["b" + str(l)] = np.zeros((layer_size, 1))
