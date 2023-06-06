import unittest
import random
from src.DataStructures.Heap import Heap


class HeapTest(unittest.TestCase):
    def test_1(self):
        input_arr = [1, 5, 3, 4, 0]
        heap = Heap()
        for item in input_arr:
            heap.add(item)

        result_arr = sorted(input_arr)
        self.assertEqual(len(input_arr), len(heap))
        for res in result_arr:
            item = heap.pop()

            self.assertEqual(res, item)

        self.assertEqual(len([]), len(heap))

    def test_2(self):
        input_arr = [1, 5, 3, 4, 0]
        heap = Heap()
        for item in input_arr:
            heap[item] = item

        self.assertEqual(len(input_arr), len(heap))
        self.assertEqual(3, heap[3])
        del heap[3]

        result_arr = [0, 1, 4, 5]
        self.assertEqual(len(result_arr), len(heap))
        for res in result_arr:
            item = heap.pop()
            self.assertEqual(res, item)

        self.assertEqual(len([]), len(heap))

    def test_3(self):
        input_arr = [1, 5, 3, 4, 0]
        heap = Heap(lambda a, b: a > b)
        for item in input_arr:
            heap.add(item)

        result_arr = sorted(input_arr, reverse=True)
        for res in result_arr:
            item = heap.pop()
            self.assertEqual(res, item)

    def test_complex(self):
        random_cof = 0.3
        for i in range(1, 100):
            input_arr = [n for n in range(1, i + 1)]
            random_arr = input_arr.copy()
            random.shuffle(random_arr)
            heap = Heap(lambda a, b: a > b)
            removals = 0

            for item in random_arr:

                heap.add(item)
                if random_cof > random.random():
                    removals += 1
                    element = heap.pop()
                    input_arr.remove(element)

            if len(input_arr) != 0:
                self.assertEqual(input_arr[len(input_arr) - 1], heap.peak())

            input_arr.reverse()
            for n in input_arr:
                m = heap.pop()
                self.assertEqual(n, m)
