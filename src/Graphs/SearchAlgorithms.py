from typing import Dict, Set
from collections import deque


class SearchAlgorithms:
    @staticmethod
    def bfs(graph: Dict[int, Set[int]], start_vertex: int) -> Set[int]:
        visited_vertexes = set()
        vertexes_queue = deque()

        vertexes_queue.append(start_vertex)

        while len(vertexes_queue) != 0:
            current_vertex = vertexes_queue.popleft()
            visited_vertexes.add(current_vertex)
            vertexes_queue.extend(
                connected_vertex for connected_vertex in graph[current_vertex]
                if connected_vertex not in visited_vertexes
                and connected_vertex not in vertexes_queue
            )

        return visited_vertexes

    @staticmethod
    def dfs(graph: Dict[int, Set[int]], start_vertex: int) -> Set[int]:
        visited_vertexes = set()
        vertexes_stack = [start_vertex]

        while len(vertexes_stack) != 0:
            current_vertex = vertexes_stack.pop()
            if current_vertex in visited_vertexes:
                continue
            visited_vertexes.add(current_vertex)
            vertexes_stack.extend(graph[current_vertex])

        return visited_vertexes
