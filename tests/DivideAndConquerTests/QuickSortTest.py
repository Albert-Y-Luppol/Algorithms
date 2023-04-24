import unittest
from typing import List, Callable

from src.DivideAndConquer.QuickSort import QuickSort


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

    def test_standard_hard(self):
        with open('./test_data/quick_sort.txt', 'r') as file:
            input_content = file.read()


        fn_input = list(map(int, input_content.split()))
        fn_output = sorted(fn_input)

        self.assertEqual(fn_output, QuickSort.sort(fn_input))

    def test_count_comparisons_0(self):
        input_arr = [1]
        fn_input = list(input_arr)
        expected_output = 0

        self.assertEqual(expected_output, QuickSort.countComparisons(fn_input))

    def test_count_comparisons_1(self):
        input_arr = [1, 2]
        fn_input = list(input_arr)
        expected_output = 1

        self.assertEqual(expected_output, QuickSort.countComparisons(fn_input))

    def test_count_comparisons_2(self):
        input_arr = [1, 2, 3, 4]
        fn_input = list(input_arr)
        partition_fn = lambda arr, start, end: start
        expected_output = 6

        self.assertEqual(expected_output, QuickSort.countComparisons(fn_input, partition_fn))

    def test_count_comparisons_3(self):
        input_arr = [1, 2, 3, 4]
        fn_input = list(input_arr)
        partition_fn = lambda arr, start, end: end
        expected_output = 6

        self.assertEqual(expected_output, QuickSort.countComparisons(fn_input, partition_fn))

    def test_count_comparisons_4(self):
        input_arr = [1, 2, 3, 4]
        fn_input = list(input_arr)
        partition_fn = lambda arr, start, end: sorted(
            zip(
                [start, end, start + end // 2],
                [arr[start], arr[end], arr[start + end // 2]],
            ),
            key=lambda p: p[1],
        )[1][0]
        expected_output = 4

        self.assertEqual(expected_output, QuickSort.countComparisons(fn_input, partition_fn))

    def test_count_comparisons_hard_start(self):
        with open('./test_data/quick_sort.txt', 'r') as file:
            input_content = file.read()

        partition_fn: Callable[[List[int], int, int], int] = lambda arr, start, end: start

        fn_input = list(map(int, input_content.split()))
        fn_output = 162085

        self.assertEqual(fn_output, QuickSort.countComparisons(fn_input, partition_fn))

    def test_count_comparisons_hard_end(self):
        with open('./test_data/quick_sort.txt', 'r') as file:
            input_content = file.read()

        partition_fn = lambda arr, start, end: end

        fn_input = list(map(int, input_content.split()))
        fn_output = 164123

        self.assertEqual(fn_output, QuickSort.countComparisons(fn_input, partition_fn))

    def test_count_comparisons_hard_middle(self):
        with open('./test_data/quick_sort.txt', 'r') as file:
            input_content = file.read()

        partition_fn = lambda arr, start, end: sorted(
            zip(
                [start, end, (start + end) // 2],
                [arr[start], arr[end], arr[(start + end) // 2]],
            ),
            key=lambda p: p[1],
        )[1][0]

        fn_input = list(map(int, input_content.split()))
        fn_output = 138382

        self.assertEqual(fn_output, QuickSort.countComparisons(fn_input, partition_fn))


if __name__ == '__main__':
    unittest.main()
