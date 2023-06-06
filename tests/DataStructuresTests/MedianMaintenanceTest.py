import unittest
import random
from src.DataStructures.MedianMaintenance import MedianMaintenance


class MedianMaintenanceTest(unittest.TestCase):
    def test_1(self):
        input_arr = [1, 5, 3, 4, 0]
        mm = MedianMaintenance()
        for item in input_arr:
            mm.add(item)
        self.assertEqual(3, mm.median())

    def test_2(self):
        input_arr = [1, 2, 3, 4, 5, 6, 7, 8]
        mm = MedianMaintenance()
        for item in input_arr:
            mm.add(item)
        self.assertEqual(4, mm.median())

    def test_3(self):
        input_arr = [1]
        mm = MedianMaintenance()
        for item in input_arr:
            mm.add(item)
        self.assertEqual(1, mm.median())

    def test_4(self):
        input_arr = [11, 10, 5, 6, 2, 9, 7, 1, 3, 4, 8]
        mm = MedianMaintenance()
        for item in input_arr:
            mm.add(item)
        self.assertEqual(6, mm.median())

    def test_5(self):
        input_arr = [1, 2, 2, 2, 2, 3, 4, 4, 4, 4, 4]
        mm = MedianMaintenance()
        for item in input_arr:
            mm.add(item)
        self.assertEqual(3, mm.median())

    def test_6(self):
        input_arr = [2, 1]
        mm = MedianMaintenance()
        for item in input_arr:
            mm.add(item)
        self.assertEqual(1, mm.median())

    def test_load(self):
        for i in range(1, 100):
            input_arr = [num for num in range(1, i+1)]
            random.shuffle(input_arr)
            sorted_arr = []
            mm = MedianMaintenance()
            for n in input_arr:
                sorted_arr.append(n)
                sorted_arr = sorted(sorted_arr)

                mm.add(n)

                mi = (len(sorted_arr) - 1) // 2
                sam = sorted_arr[mi]
                mmm = mm.median()

                self.assertEqual(sam, mmm)

    def test_large(self):
        with open('./test_data/maintain_median.txt', 'r') as file:
            input_str = file.read()
        input_arr = [int(n.strip()) for n in input_str.strip().split('\n')]
        mm = MedianMaintenance()
        result = 0
        for item in input_arr:
            mm.add(item)
            result += mm.median()

        self.assertEqual(1213, result % 10000)
