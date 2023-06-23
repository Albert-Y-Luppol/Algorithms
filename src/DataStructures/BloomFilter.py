import bitarray
import numpy as np
import hashlib
from typing import Any
from scipy.optimize import minimize, Bounds


class BloomFilter:
    def __init__(self, elements_number=1001, bits_per_element=8):
        self.size = elements_number
        self.hash_functions = []

        # Optimal number of hash functions
        bounds = Bounds([1], [np.inf])
        result = minimize(
            lambda k: (1 - np.exp(-k/bits_per_element))**k,
            x0=np.array([1]),
            method='L-BFGS-B',
            bounds=bounds,
        )
        self.hash_fns_number = int(round(result.x[0]))
        # print(f"Optimal number of hash functions: {self.hash_fns_number}")

        for i in range(self.hash_fns_number):
            self.hash_functions.append(lambda x: int(hashlib.sha256(f"{x}{i}".encode()).hexdigest(), 16) % (elements_number * bits_per_element))

        self.bits = bitarray.bitarray(elements_number * bits_per_element)
        self.bits.setall(False)

    def add(self, value: Any):
        for hash_function in self.hash_functions:
            self.bits[hash_function(value)] = True

    def lookup(self, value: Any):
        for hash_function in self.hash_functions:
            if not self.bits[hash_function(value)]:
                return False
        return True
