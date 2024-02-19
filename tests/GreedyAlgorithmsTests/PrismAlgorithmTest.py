import unittest
from GreedyAlgorithms.PrismAlgorithm import PrismAlgorithm, Edge, construct_graph


class PrismAlgorithmTest(unittest.TestCase):
    def test_1(self):
        edges = [
            Edge(1, 2, 1),
            Edge(2, 4, 3),
            Edge(2, 3, 2),
            Edge(4, 6, 1),
            Edge(6, 5, 2),
            Edge(4, 5, 6),
            Edge(1, 3, 3),
            Edge(3, 5, 4),
        ]

        prism = PrismAlgorithm(construct_graph(edges))
        print(prism.get_mst_edges())
        self.assertEqual(9, prism.get_mst_cost())

    def test_2(self):
        with open('./test_data/prism.txt', 'r') as file:
            input_str = file.read()

        rows = [row.strip().split(' ') for row in input_str.strip().split('\n') if len(row.strip().split(' ')) == 3]
        edges = [Edge(int(from_v), int(to_v), int(w)) for from_v, to_v, w in rows]
        prism = PrismAlgorithm(construct_graph(edges))

        self.assertEqual(-3612829, prism.get_mst_cost())
