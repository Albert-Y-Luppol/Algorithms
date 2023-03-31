import unittest

from src.Toolbox.FibonacciNumbers import FibonacciNumbers


class FibonacciNumbersTest(unittest.TestCase):
    def test_generate_range_1(self):
        fn_output = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
        self.assertEqual(fn_output, FibonacciNumbers.generateFibonacciSequence(10))

    def test_generate_range_2(self):
        fn_output = []

        self.assertEqual(FibonacciNumbers.generateFibonacciSequence(0), fn_output)

    def test_generate_range_3(self):
        fn_output = [1]

        self.assertEqual(FibonacciNumbers.generateFibonacciSequence(1), fn_output)

    def test_generate_range_4(self):
        fn_output = [1, 1]

        self.assertEqual(FibonacciNumbers.generateFibonacciSequence(2), fn_output)

    def test_sum_first_n_fibonacci_numbers_1(self):
        fn_output = 2
        self.assertEqual(FibonacciNumbers.sumFirstNFibonacciNumbers(2), fn_output)

    def test_sum_first_n_fibonacci_numbers_2(self):
        fn_output = 0
        self.assertEqual(FibonacciNumbers.sumFirstNFibonacciNumbers(0), fn_output)

    def test_sum_first_n_fibonacci_numbers_3(self):
        fn_output = 20
        self.assertEqual(FibonacciNumbers.sumFirstNFibonacciNumbers(6), fn_output)

    def test_last_digit_of_nth_fibonacci_number_1(self):
        fn_input = 0
        fn_output = None
        self.assertEqual(FibonacciNumbers.lastDigitOfNthFibonacciNumber(fn_input), fn_output)

    def test_last_digit_of_nth_fibonacci_number_2(self):
        fn_input = 1
        fn_output = 1
        self.assertEqual(FibonacciNumbers.lastDigitOfNthFibonacciNumber(fn_input), fn_output)

    def test_last_digit_of_nth_fibonacci_number_3(self):
        fn_input = 2
        fn_output = 1
        self.assertEqual(FibonacciNumbers.lastDigitOfNthFibonacciNumber(fn_input), fn_output)

    def test_last_digit_of_nth_fibonacci_number_4(self):
        fn_input = 10
        fn_output = 5
        self.assertEqual(fn_output, FibonacciNumbers.lastDigitOfNthFibonacciNumber(fn_input))

    def test_nth_fibonacci_number_1(self):
        fn_input = 1
        fn_output = 1
        self.assertEqual(fn_output, FibonacciNumbers.nthFibonacciNumber(fn_input))

    def test_nth_fibonacci_number_2(self):
        fn_input = 10
        fn_output = 55
        self.assertEqual(fn_output, FibonacciNumbers.nthFibonacciNumber(fn_input))

    def test_nth_fibonacci_number_3(self):
        fn_input = 0
        fn_output = 0
        self.assertEqual(fn_output, FibonacciNumbers.nthFibonacciNumber(fn_input))

    def test_sum_of_nth_fibonacci_numbers_1(self):
        fn_input = 1
        fn_output = 1
        self.assertEqual(fn_output, FibonacciNumbers.sumOfNthFibonacciNumbers(fn_input))

    def test_sum_of_nth_fibonacci_numbers_2(self):
        fn_output = 20
        self.assertEqual(fn_output, FibonacciNumbers.sumOfNthFibonacciNumbers(6))

    def test_sum_of_nth_fibonacci_numbers_3(self):
        fn_output = 0
        self.assertEqual(fn_output, FibonacciNumbers.sumOfNthFibonacciNumbers(0))


if __name__ == '__main__':
    unittest.main()
