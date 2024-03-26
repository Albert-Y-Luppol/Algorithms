import unittest
from src.DynamicProgramming.OptimalBinarySearchTree import OptimalBinarySearchTree


class OptimalBinarySearchTreeTest(unittest.TestCase):
    def test_0(self):
        weights = [0.1, 0.2, 0.3, 0.4]
        obst = OptimalBinarySearchTree(weights)
        self.assertEqual(1.8, obst.cost)

    def test_1(self):
        weights = [0.05, 0.4, 0.08, 0.04, 0.1, 0.1, 0.23]
        obst = OptimalBinarySearchTree(weights)
        self.assertEqual(2.18, obst.cost)

    def test_3(self):
        weights = [0.2, 0.05, 0.17, 0.1, 0.2, 0.03, 0.25]
        obst = OptimalBinarySearchTree(weights)
        self.assertEqual(2.23, obst.cost)
        