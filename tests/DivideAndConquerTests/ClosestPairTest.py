import unittest

from src.DivideAndConquer.ClosestPair import Pair, Point, ClosestPair


class ClosestPairTest(unittest.TestCase):
    def test_standard_1(self):
        plain_data = [(1, 1), (3, 3), (6, 1), (1, 9), (1, 2), (5, 6), (12, 22)]
        fn_input = list(map(lambda p: Point(p[0], p[1]), plain_data))
        fn_output = Pair[Point](Point(1, 1), Point(1, 2))

        self.assertEqual(ClosestPair.run(fn_input), fn_output)

    def test_standard_2(self):
        plain_data = [(1, 1), (3, 3), (6, 1), (1, 9), (3, 2), (5, 6), (12, 22)]
        fn_input = list(map(lambda p: Point(p[0], p[1]), plain_data))
        fn_output = Pair[Point](Point(3, 2), Point(3, 3))
        self.assertEqual(ClosestPair.run(fn_input), fn_output)


if __name__ == '__main__':
    unittest.main()
