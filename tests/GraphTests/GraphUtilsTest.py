import unittest
from typing import Dict, Set
from Graphs.GraphUtils import GraphUtils


class GraphUtilsTest(unittest.TestCase):
    def test_str_to_adjacency_list_conversion_1(self):
        input_str = '1 2\n2 3\n3 1'
        expected_output = {1: [2], 2: [3], 3: [1]}
        self.assertEqual(expected_output, GraphUtils.strToAdjacencyList(input_str))

    def test_adjacency_list_to_str_conversion_1(self):
        input_str = {1: [2], 2: [3], 3: [1]}
        expected_output = '1 2\n2 3\n3 1'
        self.assertEqual(expected_output, GraphUtils.adjacencyListStringify(input_str))

    @staticmethod
    def __check_for_unidirectional_edges(graph: Dict[int, Set[int]]) -> bool:
        for vertex, connected_vertexes in graph.items():
            for connected_vertex in connected_vertexes:
                if vertex not in graph[connected_vertex]:
                    return False
        return True

    def test_generate_undirected_graph_1(self):
        for i in range(1, 50):
            graph = GraphUtils.generate_undirected_graph(i)
            self.assertEqual(True, GraphUtilsTest.__check_for_unidirectional_edges(graph))
