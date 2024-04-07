from src.helpers.types import AdjacencyList
from copy import deepcopy
from src.helpers.monitoring import print_progress_bar


class FloydWarshallAlgorithm:
    def __init__(self, graph: AdjacencyList, loader=False):
        self.has_negative_cycle = False
        vertices = graph.keys()
        vertices_count = len(vertices)
        last_paths_length = [[float('inf')]*vertices_count for _ in range(vertices_count)]
        vertex_between = [[None] * vertices_count for _ in range(vertices_count)]
        for head in vertices:
            for tail in vertices:
                if tail == head:
                    last_paths_length[tail - 1][head - 1] = 0
                elif head in graph[tail]:
                    last_paths_length[tail - 1][head - 1] = graph[tail][head]

        for k in range(1, vertices_count + 1):
            current_paths_length = deepcopy(last_paths_length)
            for i in vertices:
                for j in vertices:
                    if current_paths_length[i - 1][j - 1] > last_paths_length[i - 1][k - 1] + last_paths_length[k - 1][j - 1]:
                        current_paths_length[i - 1][j - 1] = last_paths_length[i - 1][k - 1] + last_paths_length[k - 1][j - 1]
                        vertex_between[i - 1][j - 1] = k
                        if i == j and current_paths_length[i - 1][j - 1] < 0:
                            self.has_negative_cycle = True

                    if self.has_negative_cycle:
                        break
                if self.has_negative_cycle:
                    break
            if self.has_negative_cycle:
                break

            last_paths_length = current_paths_length
            if loader:
                print_progress_bar(k, vertices_count, prefix='Floyd-Warshall Algorithm')

        self.paths_length = last_paths_length
        self.vertex_between = vertex_between

    def path_length_between(self, tail: int, head: int) -> float:
        return self.paths_length[tail - 1][head - 1]

    def path_between(self, tail: int, head: int) -> [int]:
        if self._vertex_between(tail, head) is None:
            return [tail, head]

        between = self._path_between(tail, head)
        return [tail, *between, head]

    def _path_between(self, tail: int, head: int) -> [int]:
        vertex_between = self._vertex_between(tail, head)
        if vertex_between is None:
            return []
        else:
            left = self._path_between(tail, vertex_between)
            right = self._path_between(vertex_between, head)
            return [*left, vertex_between, *right]

    def _vertex_between(self, tail: int, head: int) -> int | None:
        return self.vertex_between[tail - 1][head - 1]
