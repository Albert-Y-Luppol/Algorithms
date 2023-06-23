import unittest
import string
import random
import math

from src.DataStructures.BloomFilter import BloomFilter


class BloomFilterTest(unittest.TestCase):
    def test_1(self):
        bf = BloomFilter(10, 8)
        bf.add("hello")
        self.assertTrue(bf.lookup("hello"))

    def test_2(self):
        def generate_random_string(length):
            letters = string.ascii_letters
            random_string = ''.join(random.choice(letters) for _ in range(length))
            return random_string

        elements_number = 1000000
        bits_per_element = 16
        bf = BloomFilter(elements_number, bits_per_element)
        keys = {generate_random_string(10) for _ in range(elements_number)}
        for key in keys:
            bf.add(key)

        false_positives = 0
        for _ in range(1000):
            key = generate_random_string(10)
            if bf.lookup(key) and key not in keys:
                false_positives += 1

        for key in keys:
            self.assertTrue(bf.lookup(key))

        # print(f"False positives: {false_positives}")
        error_chance = (1 - math.exp(-bf.hash_fns_number / bits_per_element)) ** bf.hash_fns_number
        # print(f"Error chance: {error_chance}, expected: {error_chance * elements_number}, actual: {false_positives}")
        self.assertTrue(false_positives < error_chance * elements_number)
