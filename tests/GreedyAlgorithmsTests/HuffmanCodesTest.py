import unittest
from GreedyAlgorithms.HuffmanCodes import HoffmanCodes


class ClusteringAlgorithmTest(unittest.TestCase):
    def test_1(self):
        weights = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        hc = HoffmanCodes(weights)
        # print(hc.bst)

        min_h, max_h = hc.get_bst_attributes()

        self.assertEqual(2, min_h)
        self.assertEqual(5, max_h)

    def test_2(self):
        with open('./test_data/huffman.txt', 'r') as file:
            input_str = file.read()

        weights = [int(row.strip()) for row in input_str.strip().split('\n')[1:]]

        hc = HoffmanCodes(weights)

        min_h, max_h = hc.get_bst_attributes()

        self.assertEqual(9, min_h)
        self.assertEqual(19, max_h)
