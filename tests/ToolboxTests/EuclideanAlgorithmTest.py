import unittest

from src.Toolbox.EuclideanAlgorithm import EuclideanAlgorithm


class EuclideanAlgorithmTest(unittest.TestCase):
    def test_greatest_common_divisor_1(self):
        fn_output = 1
        self.assertEqual(fn_output, EuclideanAlgorithm.greatestCommonDivisor(1, 0))

    def test_greatest_common_divisor_2(self):
        fn_output = 9
        self.assertEqual(fn_output, EuclideanAlgorithm.greatestCommonDivisor(9, 81))

    def test_greatest_common_divisor_3(self):
        fn_output = 135
        self.assertEqual(fn_output, EuclideanAlgorithm.greatestCommonDivisor(135, 135))

    def test_greatest_common_divisor_4(self):
        fn_output = 5
        self.assertEqual(fn_output, EuclideanAlgorithm.greatestCommonDivisor(10, 15))

    def test_least_common_divisor_1(self):
        fn_output = 1
        self.assertEqual(fn_output, EuclideanAlgorithm.leastDividendForTwoNumbers(1, 0))

    def test_least_common_divisor_2(self):
        fn_output = 81
        self.assertEqual(fn_output, EuclideanAlgorithm.leastDividendForTwoNumbers(9, 81))

    def test_least_common_divisor_3(self):
        fn_output = 135
        self.assertEqual(fn_output, EuclideanAlgorithm.leastDividendForTwoNumbers(135, 135))

    def test_least_common_divisor_4(self):
        fn_output = 30
        self.assertEqual(fn_output, EuclideanAlgorithm.leastDividendForTwoNumbers(10, 15))


if __name__ == '__main__':
    unittest.main()
