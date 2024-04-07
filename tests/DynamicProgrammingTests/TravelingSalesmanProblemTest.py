import unittest
import matplotlib.pyplot as plt
from src.DynamicProgramming.TravelingSalesmanProblem import TSPBrutForce, TSPDynamicProgramming
from src.helpers.transformers import points_to_graph_2d
import tracemalloc


class TravelingSalesmanProblemTest(unittest.TestCase):
    def test_0(self):
        points = [(0, 0), (1, 0), (1, 1), (0, 1)]
        graph = points_to_graph_2d(points)
        tsp = TSPBrutForce(graph)
        self.assertEqual(4, tsp.shortest_path_value())

    def test_1(self):
        graph = {
            1: {2: 2, 3: 4, 4: 1},
            2: {1: 2, 3: 5, 4: 3},
            3: {1: 4, 2: 5, 4: 6},
            4: {1: 1, 2: 3, 3: 6},
        }
        tsp = TSPBrutForce(graph)
        self.assertEqual(13, tsp.shortest_path_value())

    def test_2(self):
        with open('test_data/tsp.txt') as file:
            input_str = file.read()

        point_strs = input_str.strip().split('\n')[1:]
        points = [tuple(map(float, s.strip().split())) for s in point_strs]
        graph = points_to_graph_2d(points)
        tsp = TSPBrutForce(graph, loader=True)
        self.assertEqual(10, tsp.shortest_path_value())

    def test_3(self):
        points = [(0, 0), (1, 0), (1, 1), (0, 1)]
        graph = points_to_graph_2d(points)
        tsp = TSPDynamicProgramming(graph)
        self.assertEqual(4, tsp.shortest_path_weight)

    def test_4(self):
        points = [
            (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
            (7, 1), (6, 1), (5, 1), (4, 1), (3, 1), (2, 1), (1, 1), (0, 1),
        ]

        graph = points_to_graph_2d(points)

        tracemalloc.start()
        tsp_low = TSPDynamicProgramming(graph, loader=True, short_on_resources=True)
        _, peak_low = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        tracemalloc.start()
        tsp_high = TSPDynamicProgramming(graph, loader=True)
        _, peak_high = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        print(f'{peak_high} > {peak_low}')
        self.assertEqual(16, tsp_low.shortest_path_weight, tsp_high.shortest_path_weight)
        self.assertTrue(peak_low < peak_high)

    def test_5(self):
        graph = {
            0: {1: 2, 2: 4, 3: 1},
            1: {0: 2, 2: 5, 3: 3},
            2: {0: 4, 1: 5, 3: 6},
            3: {0: 1, 1: 3, 2: 6},
        }

        tsp = TSPDynamicProgramming(graph, short_on_resources=True)

        self.assertEqual(13, tsp.shortest_path_weight)

    def test_6(self):
        with open('test_data/tsp.txt') as file:
            input_str = file.read()

        point_strs = input_str.strip().split('\n')[1:]
        points = [tuple(map(float, s.strip().split())) for s in point_strs]

        print_points = False

        if print_points:
            x_coordinates = [point[0] for point in points]
            y_coordinates = [point[1] for point in points]
            plt.scatter(x_coordinates, y_coordinates, c='green')
            plt.title(f'{len(points)} Target Locations:')
            plt.xlabel('X Coordinate')
            plt.ylabel('Y Coordinate')
            plt.show()

        graph = points_to_graph_2d(points)
        tsp = TSPDynamicProgramming(graph, loader=True, short_on_resources=True)
        self.assertEqual(1, tsp.shortest_path_weight)
