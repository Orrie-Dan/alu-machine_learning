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

        if not all(isinstance(n, int) and n > 0 for n in layers):
            raise TypeError("layers must be a list of positive integers")

        self.nx = nx
        self.layers = layers

        self.__L = len(layers)
        self.__cache = {}
        self.__weights = {}

        for l in range(1, self.__L + 1):
            n = layers[l - 1]
            prev = nx if l == 1 else layers[l - 2]

            # He initialization
            self.__weights["W" + str(l)] = (
                np.random.randn(n, prev) * np.sqrt(2 / prev)
            )
            self.__weights["b" + str(l)] = np.zeros((n, 1))

    @property
    def L(self):
        """Number of layers"""
        return self.__L

    @property
    def cache(self):
        """Cache getter"""
        return self.__cache

    @property
    def weights(self):
        """Weights getter"""
        return self.__weights
