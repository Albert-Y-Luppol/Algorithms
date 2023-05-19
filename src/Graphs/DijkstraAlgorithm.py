from typing import Dict
from heapdict import heapdict


class DijkstraAlgorithm:
    @staticmethod
    def get_shortest_paths(graph: Dict[int, Dict[int, int]], init_vertex=1) -> Dict[int, int]:
        result: Dict[int, int] = {}
        heap = heapdict()
        heap[init_vertex] = 0
        while len(heap) > 0:
            current_vertex, path_length = heap.popitem()
            result[current_vertex] = path_length

            for target_vertex, weight in graph[current_vertex].items():
                if target_vertex in result:
                    continue

                if target_vertex not in heap or (target_vertex in heap and heap[target_vertex] > path_length + weight):
                    heap[target_vertex] = path_length + weight

        return result
