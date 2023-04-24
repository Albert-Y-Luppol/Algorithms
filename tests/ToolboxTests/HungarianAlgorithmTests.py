import unittest

from src.Toolbox.HungarianAlgorithm import HungarianAlgorithm


class HungarianAlgorithmTest(unittest.TestCase):
    def test_simple_1(self):
        fn_input = [
            '2 32 454',
            '23 232 252',
            '52 45 25',
        ]
        fn_output = '(1-2)(2-1)(3-3)'
        self.assertEqual(fn_output, HungarianAlgorithm.optimal_assignment(fn_input))


if __name__ == '__main__':
    unittest.main()
