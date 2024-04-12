import math

from src.helpers.types import AdjacencyList
from src.helpers.monitoring import print_progress_bar, print_monitor
from itertools import combinations
from math import comb
from typing import Tuple, Set


class PathCombination:
    def __init__(self, combination: [int], weight: int | float):
        self.combination = combination
        self.weight = weight

    def __str__(self):
        return f"PathCombination(combination={self.combination}, weight={self.weight})"

    def __repr__(self):
        return self.__str__()  # Or return the string directly


class TSPBrutForce:
    def __init__(self, graph: AdjacencyList, loader=False):
        initial_node = list(graph.keys())[0]
        prev_path_combinations: [PathCombination] = [PathCombination([initial_node], 0)]
        nodes_amount = len(graph)
        for step in range(1, nodes_amount):
            if loader:
                print_progress_bar(step, total=nodes_amount)

            cur_path_combinations = []

            for path in prev_path_combinations:
                tail = path.combination[-1]
                edges = graph[tail]
                for head, edge_weight in edges.items():
                    if head not in path.combination:
                        option_combination = path.combination.copy()
                        option_combination.append(head)
                        option_weight = path.weight + edge_weight
                        cur_path_combinations.append(PathCombination(option_combination, option_weight))

            prev_path_combinations = cur_path_combinations

        paths: [PathCombination] = []
        for path in prev_path_combinations:
            tail = path.combination[-1]
            if initial_node in graph[tail]:
                path_combination = path.combination.copy()
                path_combination.append(initial_node)
                paths.append(
                    PathCombination(
                        path_combination,
                        path.weight + graph[tail][initial_node],
                    ),
                )
        self.paths = paths
        self.shortest_path = min(paths, key=lambda x: x.weight)

    def shortest_path_value(self) -> int:
        return self.shortest_path.weight


class TSPDynamicProgramming:
    def __init__(self, graph: AdjacencyList, loader=False, short_on_resources=False):
        initial_vertex = list(graph.keys())[0]
        other_vertices = [v for v in graph.keys() if v != initial_vertex]
        vertices_amount = len(graph)

        dp = {}
        last_dp = {}
        for v in other_vertices:  # base case
            dp[(1 << v, v)] = graph[initial_vertex][v] if short_on_resources else (
                graph[initial_vertex][v], initial_vertex)

        iteration = 0
        total_iterations = sum(comb(vertices_amount - 1, m) for m in range(2, vertices_amount))
        for m in range(2, vertices_amount):  # all combinations
            if short_on_resources:
                memo = last_dp
                last_dp = dp
                dp = memo
                dp.clear()  # memory optimization

            for S in combinations(other_vertices, m):
                if loader:
                    iteration += 1
                    print_monitor(iteration, total_iterations)

                bits = 0
                for bit in S:
                    bits |= 1 << bit

                for j in S:
                    if j == initial_vertex:
                        continue

                    prev_bits = bits & ~(1 << j)
                    min_path = float('inf') if short_on_resources else (float('inf'), 0)

                    for k in S:
                        if k == j or j not in graph[k]:
                            continue

                        min_path = min(
                            min_path,
                            (
                                last_dp[(prev_bits, k)] + graph[k][j]
                                if short_on_resources
                                else (dp[(prev_bits, k)][0] + graph[k][j], k)
                            )
                        )

                    dp[(bits, j)] = min_path

        shortest_path_weight = float('inf') if short_on_resources else (float('inf'), 0)
        for v in graph[initial_vertex].keys():  # final step - back to initial vertex
            prev_bits = 2 ** vertices_amount - 2
            shortest_path_weight = min(
                (
                    dp[(prev_bits, v)] + graph[v][initial_vertex]
                    if short_on_resources else
                    (dp[(prev_bits, v)][0] + graph[v][initial_vertex], v)
                ),
                shortest_path_weight,
            )

        if not short_on_resources:
            self.graph = graph
            self.db = dp

        self.shortest_path_weight = shortest_path_weight if short_on_resources else shortest_path_weight[0]

        if not short_on_resources:
            # path reconstruction
            path = [initial_vertex]
            last_vertex = shortest_path_weight[1]
            path.append(last_vertex)
            bits = 2 ** vertices_amount - 2
            while bits > 0:
                prev_vertex = dp[(bits, last_vertex)][1]
                bits = bits & ~(1 << last_vertex)
                last_vertex = prev_vertex
                path.append(last_vertex)

            self.shortest_path = path


class TSPHeuristicNearestNeighbor:
    def __init__(self, points: [Tuple[float, float]], loader=False):
        points_amount = len(points)

        P = [(i, points[i])for i in range(points_amount)]
        Px = sorted(P, key=lambda p: p[1][0])   # sorted by x coordinate
        Py = sorted(P, key=lambda p: p[1][1])   # sorted by y coordinate

        for i in range(points_amount):
            P[i] = points[i]

        del P

        Px_index_map = {}
        for i in range(points_amount):
            point_key, _ = Px[i]
            Px_index_map[point_key] = i

        Py_index_map = {}
        for i in range(points_amount):
            point_key, _ = Py[i]
            Py_index_map[point_key] = i

        path_length = 0
        initial_point = Px[Px_index_map[0]]
        path = [initial_point]
        visited = {initial_point[0]}
        current_point = initial_point

        total_iterations = points_amount
        iteration = 0

        while len(visited) < points_amount:
            next_point, distance = self.__get_closest_point(
                Px,
                Py,
                current_point,
                Px_index_map[current_point[0]],
                Py_index_map[current_point[0]],
                visited,
            )

            visited.add(next_point[0])
            path_length += distance
            current_point = next_point
            path.append(next_point)
            if loader:
                iteration += 1
                print_progress_bar(iteration, total_iterations)

        last_distance = self.__get_distance_between_points(current_point[1], initial_point[1])
        self.path_length = path_length + last_distance
        self.path = path

    @staticmethod
    def __get_distance_between_points(
            p1: Tuple[float, float],
            p2: Tuple[float, float],
    ) -> float:
        return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

    def __get_closest_point(
                            self,
                            Px: [Tuple[int, Tuple[float, float]]],
                            Py: [Tuple[int, Tuple[float, float]]],
                            current_point: Tuple[int, Tuple[float, float]],
                            Px_i: int,
                            Py_i: int,
                            points_to_ignore: Set[int],
                            ) -> Tuple[Tuple[int, Tuple[float, float]], float]:
        delta = float('inf')
        result: Tuple[int, Tuple[float, float]] = (0, (0, 0))
        visited = set()

        # search left
        i = Px_i - 1
        while i >= 0 and Px[Px_i][1][0] - Px[i][1][0] <= delta:
            point = Px[i]
            i -= 1
            if (
                    point[0] in points_to_ignore or
                    point[0] == result[0]
                    or point[0] in visited
            ):
                continue

            visited.add(point[0])
            distance = self.__get_distance_between_points(current_point[1], point[1])
            result, delta = self.__compare_points(delta, distance, point, result)

        # search right
        i = Px_i + 1
        while i < len(Px) and Px[i][1][0] - Px[Px_i][1][0] <= delta:
            point = Px[i]
            i += 1
            if (
                    point[0] in points_to_ignore or
                    point[0] == result[0]
                    or point[0] in visited
            ):
                continue

            visited.add(point[0])
            distance = self.__get_distance_between_points(current_point[1], point[1])
            result, delta = self.__compare_points(delta, distance, point, result)

        # search down
        i = Py_i - 1
        while i >= 0 and Py[Py_i][1][0] - Py[i][1][0] <= delta:
            point = Py[i]
            i -= 1
            if (
                    point[0] in points_to_ignore or
                    point[0] == result[0]
                    or point[0] in visited
            ):
                continue

            visited.add(point[0])
            distance = self.__get_distance_between_points(current_point[1], point[1])
            result, delta = self.__compare_points(delta, distance, point, result)

        # search up
        i = Py_i + 1
        while i < len(Py) and Py[i][1][0] - Py[Py_i][1][0] <= delta:
            point = Py[i]
            i += 1
            if (
                    point[0] in points_to_ignore or
                    point[0] == result[0]
                    or point[0] in visited
            ):
                continue

            visited.add(point[0])
            distance = self.__get_distance_between_points(current_point[1], point[1])
            result, delta = self.__compare_points(delta, distance, point, result)

        return result, delta

    @staticmethod
    def __compare_points(
            delta: float,
            distance: float,
            point: Tuple[int, Tuple[float, float]],
            closest_point: Tuple[int, Tuple[float, float]],
    ) -> Tuple[Tuple[int, Tuple[float, float]], float]:
        result = closest_point
        min_delta = delta
        if delta >= distance:
            if distance == delta:
                if result[0] > point[0]:
                    result = point
            else:
                result = point
                min_delta = distance
        return result, min_delta
