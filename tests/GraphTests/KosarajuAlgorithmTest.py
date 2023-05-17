import unittest
import timeit
import networkx as nx
import random
import re
from typing import FrozenSet
from Graphs.KosarajuAlgorithm import Graph, KosarajuAlgorithm


class KosarajuAlgorithmTest(unittest.TestCase):
    def test_recursive_1(self):
        graph = KosarajuAlgorithm.constructGraphFromEdgesList([
            (7, 1),
            (1, 4),
            (4, 7),
            (9, 7),
            (6, 9),
            (9, 3),
            (3, 6),
            (8, 6),
            (2, 8),
            (5, 2),
            (8, 5),
        ])

        expected_result = {
            frozenset([1, 7, 4]),
            frozenset([9, 6, 3]),
            frozenset([8, 5, 2]),
        }

        self.assertEqual(expected_result, KosarajuAlgorithm.findStronglyConnectedComponents(graph, recursively=True))

    def test_recursive_2(self):
        graph = KosarajuAlgorithm.constructGraphFromEdgesList([
            (1, 2),
            (2, 3),
            (3, 4),
            (3, 1),
        ])

        expected_result = {
            frozenset([1, 2, 3]),
            frozenset([4]),
        }

        self.assertEqual(expected_result, KosarajuAlgorithm.findStronglyConnectedComponents(graph, recursively=True))

    def test_recursive_3(self):
        graph = KosarajuAlgorithm.constructGraphFromEdgesList([
            (1, 2),
            (2, 3),
            (3, 1),
            (3, 4),
            (7, 3),
            (4, 7),
            (6, 4),
            (4, 5),
            (5, 6),
            (6, 7),
            (8, 6),
            (7, 8),
        ])

        expected_result = {
            frozenset([1, 2, 3, 4, 5, 6, 7, 8]),
        }

        self.assertEqual(expected_result, KosarajuAlgorithm.findStronglyConnectedComponents(graph, recursively=True))

    def test_recursive_4(self):
        graph = KosarajuAlgorithm.constructGraphFromEdgesList([
            (1, 2),
            (2, 3),
            (3, 1),
            (1, 4),
            (2, 5),
            (3, 6),
        ])

        expected_result = {
            frozenset([1, 2, 3]),
            frozenset([4]),
            frozenset([5]),
            frozenset([6]),
        }
        self.assertEqual(expected_result, KosarajuAlgorithm.findStronglyConnectedComponents(graph, recursively=True))

    def test_load_recursive(self):
        for vertices_amount in range(1, 600):
            edges_amount = random.randint(vertices_amount - 1, int(vertices_amount * (vertices_amount - 1) / 2))
            edges = self.__generate_graph_edges(vertices_amount, edges_amount)
            expected_result = self.__get_scc(edges)
            graph = KosarajuAlgorithm.constructGraphFromEdgesList(edges)
            result = KosarajuAlgorithm.findStronglyConnectedComponents(graph, recursively=True)

            self.assertEqual(expected_result, result)

    def test_iterative_1(self):
        graph = KosarajuAlgorithm.constructGraphFromEdgesList([
            (7, 1),
            (1, 4),
            (4, 7),
            (9, 7),
            (6, 9),
            (9, 3),
            (3, 6),
            (8, 6),
            (2, 8),
            (5, 2),
            (8, 5),
        ])

        expected_result = {
            frozenset([1, 7, 4]),
            frozenset([9, 6, 3]),
            frozenset([8, 5, 2]),
        }

        self.assertEqual(expected_result, KosarajuAlgorithm.findStronglyConnectedComponents(graph))

    def test_iterative_2(self):
        graph = KosarajuAlgorithm.constructGraphFromEdgesList([
            (1, 2),
            (2, 3),
            (3, 4),
            (3, 1),
        ])

        expected_result = {
            frozenset([1, 2, 3]),
            frozenset([4]),
        }

        self.assertEqual(expected_result, KosarajuAlgorithm.findStronglyConnectedComponents(graph))

    def test_iterative_3(self):
        graph = KosarajuAlgorithm.constructGraphFromEdgesList([
            (1, 2),
            (2, 3),
            (3, 1),
            (3, 4),
            (7, 3),
            (4, 7),
            (6, 4),
            (4, 5),
            (5, 6),
            (6, 7),
            (8, 6),
            (7, 8),
        ])

        expected_result = {
            frozenset([1, 2, 3, 4, 5, 6, 7, 8]),
        }

        self.assertEqual(expected_result, KosarajuAlgorithm.findStronglyConnectedComponents(graph))

    def test_iterative_4(self):
        graph = KosarajuAlgorithm.constructGraphFromEdgesList([
            (1, 2),
            (2, 3),
            (3, 1),
            (1, 4),
            (2, 5),
            (3, 6),
        ])

        expected_result = {
            frozenset([1, 2, 3]),
            frozenset([4]),
            frozenset([5]),
            frozenset([6]),
        }
        self.assertEqual(expected_result, KosarajuAlgorithm.findStronglyConnectedComponents(graph))

    def test_load_iterative(self):
        for vertices_amount in range(1, 600):
            edges_amount = random.randint(vertices_amount - 1, int(vertices_amount * (vertices_amount - 1) / 2))
            edges = self.__generate_graph_edges(vertices_amount, edges_amount)
            expected_result = self.__get_scc(edges)
            graph = KosarajuAlgorithm.constructGraphFromEdgesList(edges)
            result = KosarajuAlgorithm.findStronglyConnectedComponents(graph)

            self.assertEqual(expected_result, result)

    def test_speed_comparison(self):
        graphs_edges = [self.__generate_graph_edges(
            vertices,
            random.randint(vertices - 1, int(vertices * (vertices - 1) / 2)),
        ) for vertices in range(300, 320)]
        recursive_time = timeit.timeit(
            lambda: [KosarajuAlgorithm.findStronglyConnectedComponents(
                KosarajuAlgorithm.constructGraphFromEdgesList(edges),
                recursively=True,
            ) for edges in graphs_edges],
            number=10,
        )

        iterative_time = timeit.timeit(
            lambda: [KosarajuAlgorithm.findStronglyConnectedComponents(
                KosarajuAlgorithm.constructGraphFromEdgesList(edges),
            ) for edges in graphs_edges],
            number=10,
        )

        lib_time_iterative = timeit.timeit(
            lambda: [self.__get_scc(edges) for edges in graphs_edges],
            number=10,
        )

        lib_time_recursive = timeit.timeit(
            lambda: [self.__get_scc(edges, recursive=True) for edges in graphs_edges],
            number=10,
        )

        print(iterative_time, recursive_time, lib_time_iterative, lib_time_recursive)
        self.assertEqual(recursive_time, min(iterative_time, recursive_time, lib_time_iterative, lib_time_recursive))

    def test_time_complexity_comparison(self):
        graphs_edges = [self.__generate_graph_edges(
            vertices,
            random.randint(vertices - 1, int(vertices * (vertices - 1) / 2)),
        ) for vertices in range(100, 200)]

        recursive_times = [timeit.timeit(lambda: KosarajuAlgorithm.findStronglyConnectedComponents(
            KosarajuAlgorithm.constructGraphFromEdgesList(edges),
            recursively=True,
        ), number=10) for edges in graphs_edges]
        recursive_times_diff = [abs(j - i) for i, j in zip(recursive_times[:-1], recursive_times[1:])]
        recursive_complexity = sum(recursive_times_diff) / len(recursive_times_diff)

        iterative_times = [timeit.timeit(lambda: KosarajuAlgorithm.findStronglyConnectedComponents(
            KosarajuAlgorithm.constructGraphFromEdgesList(edges),
        ), number=10) for edges in graphs_edges]
        iterative_times_diff = [abs(j - i) for i, j in zip(iterative_times[:-1], iterative_times[1:])]
        iterative_complexity = sum(iterative_times_diff) / len(iterative_times_diff)

        lib_iterative_times = [timeit.timeit(lambda: self.__get_scc(edges), number=10) for edges in graphs_edges]
        lib_iterative_times_diff = [abs(j - i) for i, j in zip(lib_iterative_times[:-1], lib_iterative_times[1:])]
        lib_iterative_complexity = sum(lib_iterative_times_diff) / len(lib_iterative_times_diff)

        lib_recursive_times = [timeit.timeit(lambda: self.__get_scc(
            edges, recursive=True,
        ), number=10) for edges in graphs_edges]
        lib_recursive_times_diff = [abs(j - i) for i, j in zip(lib_recursive_times[:-1], lib_recursive_times[1:])]
        lib_recursive_complexity = sum(lib_recursive_times_diff) / len(lib_recursive_times_diff)

        print(recursive_complexity, iterative_complexity, lib_recursive_complexity, lib_iterative_complexity)
        self.assertEqual(
            recursive_complexity,
            min(recursive_complexity, iterative_complexity, lib_recursive_complexity, lib_iterative_complexity),
        )

    def test_large_graph_recursive(self):
        with open('./test_data/scc.txt', 'r') as file:
            input_str = file.read()
        edges = [tuple(map(int, re.split(r'\s+', edge_str.strip()))) for edge_str in input_str.strip().split('\n')]

        graph = KosarajuAlgorithm.constructGraphFromEdgesList(edges)
        scc = KosarajuAlgorithm.findStronglyConnectedComponents(graph)
        scc_length = list(map(len, scc))

        result = sorted(scc_length, reverse=True)[:min(5, len(scc_length))]
        print(result)

        expected_scc = self.__get_scc(edges)
        expected_scc_length = list(map(len, expected_scc))
        expected_result = sorted(expected_scc_length, reverse=True)[:min(5, len(expected_scc_length))]

        self.assertEqual(expected_result, result)

    @staticmethod
    def __generate_graph_edges(vertices_amount=100, edges_amount=150) -> [int]:
        vertices = range(1, vertices_amount + 1)
        edges = set()

        while len(edges) < edges_amount:
            i = random.choice(vertices)
            j = random.choice(vertices)

            if i == j:
                continue

            edges.add((i, j))

        graph = nx.DiGraph()
        graph.add_edges_from(edges)

        return list(graph.edges)

    @staticmethod
    def __get_scc(edges, recursive=False) -> FrozenSet[FrozenSet[int]]:
        graph = nx.DiGraph()
        graph.add_edges_from(edges)
        scc = nx.strongly_connected_components_recursive(graph) if recursive \
            else nx.strongly_connected_components(graph)
        return frozenset(map(frozenset, scc))
