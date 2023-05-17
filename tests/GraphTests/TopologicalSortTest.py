import unittest
from Graphs.TopologicalSort import TopologicalSort


class TopologicalSortTest(unittest.TestCase):
    def test_straightforward_algorithm_1(self):
        input_graph = {1: {2, 3}, 2: {4}, 3: {4}, 4: {}}
        expected_output = [1, 3, 2, 4]
        self.assertEqual(expected_output, TopologicalSort.straightForwardAlgorithm(input_graph))

    def test_straightforward_algorithm_2(self):
        input_graph = {1: {2, 3, 5}, 2: {4}, 3: {4}, 4: {}, 5: {}}
        expected_output = [1, 3, 2, 5, 4]
        self.assertEqual(expected_output, TopologicalSort.straightForwardAlgorithm(input_graph))

    def test_straightforward_algorithm_3(self):
        input_graph = {1: {2}, 2: {3}, 3: {1, 4}, 4: {}, 5: {}}
        try:
            TopologicalSort.straightForwardAlgorithm(input_graph)
            self.assertEqual('Error should be erased!', '')
        except Exception as e:
            self.assertEqual('There is no way to order graph with cycle in it!', e.args[0])

    def test_dfs_algorithm_1(self):
        input_graph = {1: {2, 3}, 2: {4}, 3: {4}, 4: {}}
        expected_output = [1, 3, 2, 4]
        self.assertEqual(expected_output, TopologicalSort.dfsAlgorithm(input_graph))

    def test_dfs_algorithm_2(self):
        input_graph = {1: {2, 3, 5}, 2: {4}, 3: {4}, 4: {}, 5: {}}
        expected_output = [1, 5, 3, 2, 4]
        self.assertEqual(expected_output, TopologicalSort.dfsAlgorithm(input_graph))

    def test_dfs_algorithm_3(self):
        input_graph = {1: {2, 5}, 2: {3}, 3: {1, 4, 5}, 4: {}, 5: {}}
        try:
            print(TopologicalSort.dfsAlgorithm(input_graph))
            self.assertEqual('Error should be erased!', '')
        except Exception as e:
            self.assertEqual('There is no way to order graph with cycle in it!', e.args[0])
