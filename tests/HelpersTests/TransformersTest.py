import unittest
from src.helpers.transformers import str_to_adjacency_list


class TransformersTest(unittest.TestCase):
    def test_0(self):
        s = '5 6\n1 2 -1\n2 3 2\n 1 3 3 \n 1  4  5 \n 3     4 -2\n4 5 1'
        g = str_to_adjacency_list(s)
        self.assertEqual({
            1: {2: -1, 3: 3, 4: 5},
            2: {3: 2},
            3: {4: -2},
            4: {5: 1},
            5: {}
        }, g)

