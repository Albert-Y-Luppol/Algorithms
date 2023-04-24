import unittest
from src.DivideAndConquer.RandomizedSelection import RandomizeSelection

class RandomizedSelectionTest(unittest.TestCase):
    def test_1(self):
        input_arr = [1, 2, 3, 4, 5]
        i = 4
        expected_output = 4

        self.assertEqual(expected_output, RandomizeSelection.select_ith_element(input_arr, i))

    def test_2(self):
        input_arr = [2, 4, 5, 1, 7, 9, 3, 6, 8]
        i = 5
        expected_output = 5

        self.assertEqual(expected_output, RandomizeSelection.select_ith_element(input_arr, i))

    def test_3(self):
        input_arr = [16, 14, 13, 20, 12, 17, 18, 19, 15]
        i = 5
        expected_output = 16

        self.assertEqual(expected_output, RandomizeSelection.select_ith_element(input_arr, i))

if __name__ == '__main__':
    unittest.main()