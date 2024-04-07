import unittest
import time
from src.helpers.types import AdjacencyList
from src.DynamicProgramming.BellmanFordAlgorithm import BellmanFordAlgorithm
from src.DynamicProgramming.FloydWarshallAlforithm import FloydWarshallAlgorithm
from src.DynamicProgramming.JohnsonAlgorithm import JohnsonAlgorithm
from src.helpers.transformers import str_to_adjacency_list
from src.helpers.monitoring import print_progress_bar


class ShortestPathsAlgorithmsTest(unittest.TestCase):
    def test_0_bellman_ford(self):
        graph: AdjacencyList = {
            1: {2: -1, 3: 3, 4: 5},
            2: {3: 2},
            3: {4: -2},
            4: {5: 1},
            5: {}
        }
        bf = BellmanFordAlgorithm(graph, 1)
        self.assertEqual(False, bf.has_negative_cycle)
        self.assertEqual(0, bf.path_length_to(5))
        self.assertEqual([1, 2, 3, 4, 5], bf.path_to(5))

    def test_1_bellman_ford(self):
        graph: AdjacencyList = {
            1: {2: -1, 3: 3, 4: 5},
            2: {3: 2},
            3: {4: -2},
            4: {5: 1},
            5: {2: -3}
        }
        bf = BellmanFordAlgorithm(graph, 1)
        self.assertEqual(True, bf.has_negative_cycle)

    def test_2_bellman_ford(self):
        with open('./test_data/apsp1.txt') as file:
            graph_str = file.read()

        graph = str_to_adjacency_list(graph_str)
        vertices_count = len(graph.keys())
        i = 0
        result = float('inf')
        for v in graph.keys():
            bf = BellmanFordAlgorithm(graph, v)
            if bf.has_negative_cycle:
                break

            paths_dict = bf.vertex_distances
            del paths_dict[v]
            paths = list(paths_dict.values())
            paths.append(result)

            result = min(paths)

            i += 1
            print_progress_bar(i, vertices_count)
        self.assertEqual(float('inf'), result)

    def test_3_bellman_ford(self):
        with open('./test_data/apsp2.txt') as file:
            graph_str = file.read()

        graph = str_to_adjacency_list(graph_str)
        vertices_count = len(graph.keys())
        i = 0
        result = float('inf')
        for v in graph.keys():
            bf = BellmanFordAlgorithm(graph, v)
            if bf.has_negative_cycle:
                break

            paths_dict = bf.vertex_distances
            del paths_dict[v]
            paths = list(paths_dict.values())
            paths.append(result)

            result = min(paths)

            i += 1
            print_progress_bar(i, vertices_count)
        self.assertEqual(float('inf'), result)

    def test_4_bellman_ford(self):
        with open('./test_data/apsp3.txt') as file:
            graph_str = file.read()

        graph = str_to_adjacency_list(graph_str)
        vertices_count = len(graph.keys())
        i = 0
        result = float('inf')
        for v in graph.keys():
            bf = BellmanFordAlgorithm(graph, v)
            if bf.has_negative_cycle:
                break

            paths_dict = bf.vertex_distances
            del paths_dict[v]
            paths = list(paths_dict.values())
            paths.append(result)

            result = min(paths)

            i += 1
            print_progress_bar(i, vertices_count)
        self.assertEqual(-19, result)

    def test_0_floyd_warshall(self):
        graph: AdjacencyList = {
            1: {2: -1, 3: 3, 4: 5},
            2: {3: 2},
            3: {4: -2},
            4: {5: 1},
            5: {}
        }
        fw = FloydWarshallAlgorithm(graph)
        self.assertEqual(0, fw.path_length_between(1, 5))
        self.assertEqual(1, fw.path_length_between(2, 5))
        self.assertEqual([1, 2, 3, 4, 5], fw.path_between(1, 5))
        self.assertEqual([2, 3, 4, 5], fw.path_between(2, 5))

    def test_1_floyd_warshall(self):
        graph: AdjacencyList = {
            1: {2: -1, 3: 3, 4: 5},
            2: {3: 2},
            3: {4: -2},
            4: {5: 1},
            5: {2: -3}
        }
        fw = FloydWarshallAlgorithm(graph)
        self.assertEqual(True, fw.has_negative_cycle)

    def test_2_floyd_warshall(self):
        with open('./test_data/apsp1.txt') as file:
            graph_str = file.read()

        graph = str_to_adjacency_list(graph_str)
        vertices = graph.keys()
        result = float('inf')
        fw = FloydWarshallAlgorithm(graph, loader=True)
        if not fw.has_negative_cycle:
            for i in vertices:
                for j in vertices:
                    if i != j:
                        result = min(result, fw.paths_length[i], [j])
        self.assertEqual(float('inf'), result)

    def test_3_floyd_warshall(self):
        with open('./test_data/apsp2.txt') as file:
            graph_str = file.read()

        graph = str_to_adjacency_list(graph_str)
        vertices = graph.keys()
        result = float('inf')
        fw = FloydWarshallAlgorithm(graph, loader=True)
        if not fw.has_negative_cycle:
            for i in vertices:
                for j in vertices:
                    if i != j:
                        result = min(result, fw.paths_length[i], [j])
        self.assertEqual(float('inf'), result)

    def test_4_floyd_warshall(self):
        with open('./test_data/apsp3.txt') as file:
            graph_str = file.read()

        graph = str_to_adjacency_list(graph_str)
        vertices = graph.keys()
        result = float('inf')
        fw = FloydWarshallAlgorithm(graph, loader=True)
        if not fw.has_negative_cycle:
            for i in vertices:
                for j in vertices:
                    if i != j:
                        result = min(result, fw.paths_length[i - 1][j - 1])
        self.assertEqual(-19, result)

    def test_0_johnson(self):
        graph: AdjacencyList = {
            1: {2: -1, 3: 3, 4: 5},
            2: {3: 2},
            3: {4: -2},
            4: {5: 1},
            5: {}
        }
        j = JohnsonAlgorithm(graph)
        self.assertEqual(0, j.path_length_between(1, 5))
        self.assertEqual(1, j.path_length_between(2, 5))

    def test_1_johnson(self):
        graph: AdjacencyList = {
            1: {2: -1, 3: 3, 4: 5},
            2: {3: 2},
            3: {4: -2},
            4: {5: 1},
            5: {2: -3}
        }
        j = JohnsonAlgorithm(graph)
        self.assertEqual(True, j.has_negative_cycle)

    def test_2_johnson(self):
        with open('./test_data/apsp1.txt') as file:
            graph_str = file.read()

        graph = str_to_adjacency_list(graph_str)
        vertices_count = len(graph.keys())
        i = 0
        result = float('inf')
        for v in graph.keys():
            j = JohnsonAlgorithm(graph)
            if j.has_negative_cycle:
                break

            paths_dict = j.paths_length_from(v)
            paths = list(paths_dict.values())
            paths.append(result)

            result = min(paths)

            i += 1
            print_progress_bar(i, vertices_count)
        self.assertEqual(float('inf'), result)

    def test_3_johnson(self):
        with open('./test_data/apsp2.txt') as file:
            graph_str = file.read()

        graph = str_to_adjacency_list(graph_str)
        vertices_count = len(graph.keys())
        i = 0
        result = float('inf')
        for v in graph.keys():
            j = JohnsonAlgorithm(graph)
            if j.has_negative_cycle:
                break

            paths_dict = j.paths_length_from(v)
            paths = list(paths_dict.values())
            paths.append(result)

            result = min(paths)

            i += 1
            print_progress_bar(i, vertices_count)
        self.assertEqual(float('inf'), result)

    def test_4_johnson(self):
        with open('./test_data/apsp3.txt') as file:
            graph_str = file.read()

        graph = str_to_adjacency_list(graph_str)
        vertices_count = len(graph.keys())
        i = 0
        result = float('inf')
        for v in graph.keys():
            j = JohnsonAlgorithm(graph)
            if j.has_negative_cycle:
                break

            paths_dict = j.paths_length_from(v)
            paths = list(paths_dict.values())
            paths.append(result)

            result = min(paths)

            i += 1
            print_progress_bar(i, vertices_count)
        self.assertEqual(-19, result)

    def test_load(self):
        with open('./test_data/apsp_lg.txt') as file:
            graph_str = file.read()

        graph = str_to_adjacency_list(graph_str)
        vertices_count = len(graph.keys())
        vertices = graph.keys()

        bf_time = time.time()
        index = 0
        result_bf = float('inf')
        for v in graph.keys():
            bf = BellmanFordAlgorithm(graph, v)
            if bf.has_negative_cycle:
                break

            paths_dict = bf.vertex_distances
            del paths_dict[v]
            paths = list(paths_dict.values())
            paths.append(result_bf)

            result_bf = min(paths)

            index += 1
            print_progress_bar(index, vertices_count, prefix='Bellman-Ford Algorithm')

        bf_time = time.time() - bf_time

        fw_time = time.time()
        result_fw = float('inf')
        fw = FloydWarshallAlgorithm(graph, loader=True)
        if not fw.has_negative_cycle:
            for i in vertices:
                for j in vertices:
                    if i != j:
                        result_fw = min(result_fw, fw.paths_length[i - 1][j - 1])
        fw_time = time.time() - fw_time

        j_time = time.time()
        index = 0
        result_j = float('inf')
        for v in graph.keys():
            j = JohnsonAlgorithm(graph)
            if j.has_negative_cycle:
                break

            paths_dict = j.paths_length_from(v)
            paths = list(paths_dict.values())
            paths.append(result_j)

            result_j = min(paths)

            index += 1
            print_progress_bar(index, vertices_count, prefix='Johnson Algorithm')
        j_time = time.time() - j_time
        print(f'Bellman-Ford Time = {bf_time}, Floyd-Warsaw Time = {fw_time}, Johnson Time = {j_time}')
        self.assertEqual(True, result_j == result_fw and result_fw == result_bf)
