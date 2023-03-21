import unittest
from src.DvideAndConquer.QuickSort import QuickSort


class QuickSortTest(unittest.TestCase):
    def test_standard_1(self):
        input_arr = [1, 0, 3, 2, 5, 4, 9, 8, 6, 7]
        output_arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        fn_input = list(input_arr)
        fn_output = list(output_arr)

        self.assertEqual(QuickSort.sort(fn_input), fn_output)

    def test_standard_2(self):
        input_arr = [1, 2, 3]
        output_arr = [1, 2, 3]
        fn_input = list(input_arr)
        fn_output = list(output_arr)

        self.assertEqual(QuickSort.sort(fn_input), fn_output)

    def test_standard_3(self):
        input_arr = [3, 2, 1]
        output_arr = [1, 2, 3]
        fn_input = list(input_arr)
        fn_output = list(output_arr)

        self.assertEqual(QuickSort.sort(fn_input), fn_output)

    def test_standard_4(self):
        input_arr = [2, 1]
        output_arr = [1, 2]
        fn_input = list(input_arr)
        fn_output = list(output_arr)

        self.assertEqual(fn_output, QuickSort.sort(fn_input))


if __name__ == '__main__':
    unittest.main()
