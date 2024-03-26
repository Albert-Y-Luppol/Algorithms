from src.helpers.types import AdjacencyList
from src.DynamicProgramming.BellmanFordAlgorithm import BellmanFordAlgorithm
from src.Graphs.DijkstraAlgorithm import DijkstraAlgorithm
from typing import Dict

class JohnsonAlgorithm:
    def __init__(self, graph: AdjacencyList):
        vertices = graph.keys()
        self.graph = graph
        graph[0] = {key: 0 for key in vertices}

        bf = BellmanFordAlgorithm(graph, 0)
        self.bf = bf
        self.has_negative_cycle = bf.has_negative_cycle

        del graph[0]

        if not self.has_negative_cycle:
            reweighed_graph: AdjacencyList = {}
            for tail in vertices:
                reweighed_graph[tail] = {}
                for head, weight in graph[tail].items():
                    reweighed_graph[tail][head] = weight + bf.path_length_to(tail) - bf.path_length_to(head)

            self.reweighed_graph = reweighed_graph

    def path_length_between(self, tail: int, head: int) -> int:
        paths = DijkstraAlgorithm.get_shortest_paths(self.reweighed_graph, tail)
        path_length = paths[head]
        return path_length - self.bf.path_length_to(tail) + self.bf.path_length_to(head)

    def paths_length_from(self, vertex: int) -> Dict[int, int]:
        paths = DijkstraAlgorithm.get_shortest_paths(self.reweighed_graph, vertex)
        for v in paths.keys():
            paths[v] = paths[v] - self.bf.path_length_to(vertex) + self.bf.path_length_to(v)

        return paths
