import unittest
from GreedyAlgorithms.ClusteringAlgorithm import ClusteringAlgorithm, Edge, generate_same_cluster_options


class ClusteringAlgorithmTest(unittest.TestCase):
    def test_1(self):
        edges = [
            Edge(1, 2, 3),
            Edge(2, 3, 2),
            Edge(1, 3, 2),
            Edge(3, 6, 7),
            Edge(2, 7, 8),
            Edge(7, 4, 1),
            Edge(4, 5, 2),
            Edge(5, 6, 1),
            Edge(6, 8, 12),
            Edge(8, 9, 2),
            Edge(9, 10, 2),
            Edge(10, 12, 2),
            Edge(11, 10, 1),
            Edge(5, 9, 10),
        ]

        max_distance, uf = ClusteringAlgorithm.find_max_spacing_k_clusters(edges, 3)
        print(max_distance)
        print(uf)

        self.assertEqual(7, max_distance)

    def test_2(self):
        with open('./test_data/clustering1.txt', 'r') as file:
            input_str = file.read()

        rows = [row.strip().split(' ') for row in input_str.strip().split('\n') if len(row.strip().split(' ')) == 3]
        edges = [Edge(int(from_v), int(to_v), int(w)) for from_v, to_v, w in rows]
        max_distance, uf = ClusteringAlgorithm.find_max_spacing_k_clusters(edges, 4)
        print(max_distance)
        print(uf)
        self.assertEqual(106, max_distance)

    def test_3(self):
        vertex = (False, False, False)
        expected_result = {
            (True, False, False),
            (False, True, False),
            (False, False, True),
            (True, True, False),
            (True, False, True),
            (False, True, True),
        }
        result = generate_same_cluster_options(vertex, 2)
        self.assertEqual(expected_result, result)

    def test_4(self):
        vertices = [
            (True, True, True, True, True, True, True),
            (True, False, True, True, True, True, True),
            (False, False, False, True, True, True, True),

            (True, True, False, False, False, True, True),
            (False, True, True, False, False, True, True),

            (True, True, True, True, False, False, False),
            (True, True, True, True, False, False, False),
            (True, True, True, True, False, False, False),
            (True, True, True, True, False, False, False),
        ]
        clusters_count, uf = ClusteringAlgorithm.find_max_clusters_with_min_spacing_by_hamming_distance(
            vertices,
            2,
        )
        print(clusters_count)
        self.assertEqual(3, clusters_count)

    def test_5(self):
        with open('./test_data/clustering_big.txt', 'r') as file:
            input_str = file.read()

        vertices = set([
            tuple(
                map(lambda s: bool(int(s)), row.strip().split(' '))
            ) for row in input_str.strip().split('\n') if len(row.strip().split(' ')) == 24])

        clusters_count, uf = ClusteringAlgorithm.find_max_clusters_with_min_spacing_by_hamming_distance(
            list(vertices),
            2,
        )
        print(clusters_count)
        self.assertEqual(6118, clusters_count)
