import unittest
from Graphs.SearchAlgorithms import SearchAlgorithms
from Graphs.GraphUtils import GraphUtils
from random import randint


class SearchAlgorithmsTest(unittest.TestCase):
    def test_bfs_1(self):
        input_graph = {1: {2}, 2: {3}, 3: {1}}
        initial_vertex = 1
        expected_output = {1, 2, 3}
        self.assertEqual(expected_output, SearchAlgorithms.bfs(input_graph, initial_vertex))

    def test_bfs_2(self):
        input_graph = {1: {2}, 2: {3}, 3: {1}, 4: {5}, 5: {4}}
        initial_vertex = 3
        expected_output = {1, 2, 3}
        self.assertEqual(expected_output, SearchAlgorithms.bfs(input_graph, initial_vertex))

    def test_bfs_3(self):
        input_graph = {1: {2}, 2: {3}, 3: {1}, 4: {5}, 5: {4}}
        initial_vertex = 4
        expected_output = {4, 5}
        self.assertEqual(expected_output, SearchAlgorithms.bfs(input_graph, initial_vertex))

    def test_bfs_4(self):
        input_graph = {1: set()}
        initial_vertex = 1
        expected_output = {1}
        self.assertEqual(expected_output, SearchAlgorithms.bfs(input_graph, initial_vertex))

    def test_dfs_1(self):
        input_graph = {1: {2}, 2: {3}, 3: {1}}
        initial_vertex = 1
        expected_output = {1, 2, 3}
        self.assertEqual(expected_output, SearchAlgorithms.dfs(input_graph, initial_vertex))

    def test_dfs_2(self):
        input_graph = {1: {2}, 2: {3}, 3: {1}, 4: {5}, 5: {4}}
        initial_vertex = 3
        expected_output = {1, 2, 3}
        self.assertEqual(expected_output, SearchAlgorithms.dfs(input_graph, initial_vertex))

    def test_dfs_3(self):
        input_graph = {1: {2}, 2: {3}, 3: {1}, 4: {5}, 5: {4}}
        initial_vertex = 4
        expected_output = {4, 5}
        self.assertEqual(expected_output, SearchAlgorithms.dfs(input_graph, initial_vertex))

    def test_dfs_4(self):
        input_graph = {1: set()}
        initial_vertex = 1
        expected_output = {1}
        self.assertEqual(expected_output, SearchAlgorithms.dfs(input_graph, initial_vertex))

    def test_bfs_and_dfs_1(self):
        for i in range(1, 51):
            graph = GraphUtils.generate_undirected_graph(i)
            for j in range(1, i + 1):
                initial_vertex = randint(1, i)
                self.assertEqual(
                    SearchAlgorithms.bfs(graph, initial_vertex),
                    SearchAlgorithms.dfs(graph, initial_vertex),
                )

