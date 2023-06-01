import unittest
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
