import math
import unittest
import heapdict

from src.helpers.transformers import str_to_adjacency_list, points_to_graph_2d, points_to_heaped_graph_2d


class TransformersTest(unittest.TestCase):
    def test_0_str_to_adjacency_list(self):
        s = '5 6\n1 2 -1\n2 3 2\n 1 3 3 \n 1  4  5 \n 3     4 -2\n4 5 1'
        g = str_to_adjacency_list(s)
        self.assertEqual({
            1: {2: -1, 3: 3, 4: 5},
            2: {3: 2},
            3: {4: -2},
            4: {5: 1},
            5: {}
        }, g)

    def test_0_points_to_graph_2d(self):
        points = [(0, 0), (1, 0), (1, 1), (0, 1)]
        graph = points_to_graph_2d(points)
        self.assertEqual({
            0: {1: 1, 2: math.sqrt(2), 3: 1},
            1: {0: 1, 2: 1, 3: math.sqrt(2)},
            2: {0: math.sqrt(2), 1: 1, 3: 1},
            3: {0: 1, 1: math.sqrt(2), 2: 1},
        }, graph)
