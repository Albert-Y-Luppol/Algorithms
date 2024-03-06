import unittest
from src.DynamicProgramming.KnapsackAlgorithm import KnapsackAlgorithm

class KnapsackAlgorithmTest(unittest.TestCase):
    def test_0(self):
        items = [(3, 4), (2, 3), (4, 2), (4, 3)]
        self.assertEqual(8, KnapsackAlgorithm.max_value(items, 6))
        self.assertEqual([(4, 3), (4, 2)], KnapsackAlgorithm.optimal_solution(items, 6))

    def test_1(self):
        with open('./test_data/knapsack_sm.txt', 'r') as file:
            input_str = file.read()

        items = [tuple(map(int, row.strip().split(' '))) for row in input_str.strip().split('\n')]
        capacity, _ = items.pop(0)

        self.assertEqual(2493893, KnapsackAlgorithm.max_value(items, capacity))

    def test_2(self):
        with open('./test_data/knapsack_lg.txt', 'r') as file:
            input_str = file.read()
        items = [tuple(map(int, row.strip().split(' '))) for row in input_str.strip().split('\n')]
        capacity, _ = items.pop(0)

        self.assertEqual(4243395, KnapsackAlgorithm.max_value(items, capacity, progress_bar=True))
