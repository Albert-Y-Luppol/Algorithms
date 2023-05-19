import unittest
import re
import networkx as nx
from typing import Dict
from src.Graphs.DijkstraAlgorithm import DijkstraAlgorithm


class DijkstraAlgorithmTest(unittest.TestCase):
    def test_get_shorted_paths_1(self):
        graph: Dict[int, Dict[int, int]] = {
            1: {2: 1, 3: 4},
            2: {1: 1, 3: 2, 4: 6},
            3: {1: 4, 2: 2, 4: 3},
            4: {2: 6, 3: 3},
        }

        expected_result = {1: 0, 2: 1, 3: 3, 4: 6}

        self.assertEqual(expected_result, DijkstraAlgorithm.get_shortest_paths(graph))

    def test_get_shorted_paths_2(self):
        graph: Dict[int, Dict[int, int]] = {
            1: {2: 2, 5: 1},
            2: {1: 2, 3: 4},
            3: {2: 4, 4: 1},
            4: {5: 2, 3: 1},
            5: {1: 1, 4: 2},
        }

        expected_result = {1: 0, 5: 1, 2: 2, 4: 3, 3: 4}

        self.assertEqual(expected_result, DijkstraAlgorithm.get_shortest_paths(graph))

    def test_get_shorted_paths_large(self):
        with open('./test_data/dijkstra.txt', 'r') as file:
            input_str = file.read()
        vertex_strs = [re.split(r'\s+', vertex_str.strip()) for vertex_str in input_str.strip().split('\n')]
        graph: Dict[int, Dict[int, int]] = {}
        G = nx.DiGraph()
        for vertex_str in vertex_strs:
            vertex = int(vertex_str[0])
            graph[vertex] = {}
            for head_str in vertex_str[1:]:
                head, weight = map(int, head_str.split(','))
                graph[vertex][head] = weight
                G.add_edge(vertex, head, weight=weight)

        self.assertEqual(nx.single_source_dijkstra_path_length(G, 1), DijkstraAlgorithm.get_shortest_paths(graph))
