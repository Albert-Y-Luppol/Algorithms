import unittest
import random
from src.DataStructures.BinarySearchTree import BinarySearchTree


class BinarySearchTreeTest(unittest.TestCase):
    def test_main(self):
        node_values = [6, 3, 6, 3, 4, 6, 2, 1, 9]
        bst = BinarySearchTree(lambda x: x, node_values)
        node_keys = list(map(bst.get_key, node_values))

        for key in node_keys:
            value = bst.get(key)
            self.assertEqual(key, value)
            bst.remove(key)

        for key in node_keys:
            self.assertEqual(None, bst.get(key))

    def test_rank(self):
        node_values = list(range(1, 121))
        random.shuffle(node_values)
        bst = BinarySearchTree(lambda x: x, node_values)
        for key in node_values:
            self.assertEqual(key, bst.rank(key))


