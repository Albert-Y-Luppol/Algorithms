import unittest
import string
import random
import math

from src.DataStructures.HashTable import HashTable


class HashTableTest(unittest.TestCase):
    def test_1(self):
        def hash_function(key, size):
            hash_arr = [ord(char) for char in key]
            return sum(hash_arr) % size

        def generate_random_string(length):
            letters = string.ascii_letters
            random_string = ''.join(random.choice(letters) for _ in range(length))
            return random_string

        size = 5
        key_symbol_number = 5
        elements_number = 15

        ht = HashTable(hash_function, size)
        keys = [generate_random_string(key_symbol_number) for _ in range(elements_number)]
        for key in keys:
            ht[key] = hash_function(key, size)

        print(ht)
        self.assertEqual(len(ht), elements_number)

        for key in keys:
            self.assertTrue(key in ht)
            self.assertEqual(ht[key], hash_function(key, size))

        for key in keys:
            del ht[key]
            self.assertFalse(key in ht)
            self.assertEqual(len(ht), elements_number - 1)
            elements_number -= 1

    def test_2_sum_sm(self):
        def hash_fn(key, size):
            return int(math.fmod(key, ((size + 1) // 2))) + size // 2

        nums = [-3, 1, -2, 3, 5, 5, 4, -5, 2, 0, 1, 4, 4, 3, 2, -2, -3, 4, 2, 1, 3]
        random.shuffle(nums)
        ht = HashTable(hash_fn, len(nums))
        for num in nums:
            ht[num] = num

        result = 0
        for target_sum in range(-10, 10):
            for _, x in ht:
                y = target_sum - x
                if y <= x:
                    break

                if x in ht and y in ht:
                    result += 1
                    break

        self.assertEqual(result, 17)

    def test_2_sum_lg(self):
        def hash_fn(key, size):
            return int(math.fmod(key, ((size + 1) // 2))) + size // 2

        with open('./test_data/2sum.txt', 'r') as file:
            input_str = file.read()
        nums = [int(n.strip()) for n in input_str.strip().split('\n')]

        ht = HashTable(hash_fn, len(nums))
        for num in nums:
            ht[num] = num
        result = 0
        for target_sum in range(-10000, 10001):
            for _, x in ht:
                y = target_sum - x
                if y <= x:
                    break

                if y in ht:
                    result += 1
                    break

        self.assertEqual(result, 427)
