import re
import random
from typing import Dict, List, Set


class GraphUtils:
    @staticmethod
    def strToAdjacencyList(input_str: str) -> Dict[int, List[int]]:
        return {
            int(node[0]): [int(n) for n in node[1:]] for node in (re.split(r'\s+', row.strip())
                                                                  for row in input_str.strip().split('\n'))
        }

    @staticmethod
    def adjacencyListStringify(graph: Dict[int, List[int]]) -> str:
        return '\n'.join([' '.join(str(n) for n in ({key}.union(graph[key]))) for key in graph.keys()])

    @staticmethod
    def generate_directed_graph(vertexes_amount: int) -> Dict[int, Set[int]]:
        vertexes = range(1, vertexes_amount + 1)
        graph: Dict[int, Set[int]] = {
            vertex: set(
                random.sample(
                    vertexes,
                    random.randint(0, vertexes_amount),
                ),
            ).difference({vertex})
            for vertex in vertexes
        }

        return graph

    @staticmethod
    def generate_undirected_graph(vertexes_amount: int) -> Dict[int, Set[int]]:
        graph = GraphUtils.generate_directed_graph(vertexes_amount)

        for vertex, related_vertexes in graph.items():
            for related_vertex in related_vertexes:
                graph[related_vertex].add(vertex)

        return graph
