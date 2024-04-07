from src.helpers.types import AdjacencyList
from src.helpers.monitoring import print_progress_bar, print_monitor
from itertools import combinations
from math import comb


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
