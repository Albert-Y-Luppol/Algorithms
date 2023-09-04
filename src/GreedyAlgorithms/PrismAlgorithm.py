# Minimum spanning tree
from dataclasses import dataclass
from functools import total_ordering
from typing import Self, Dict, List

from heapdict import heapdict

Graph = Dict[int, Dict[int, int]] #AdjacencyList


@total_ordering
@dataclass
class Edge:
    from_vertex: int
    to_vertex: int
    weight: int

    def __eq__(self, other: Self) -> bool:
        if isinstance(other, Edge):
            return self.weight == other.weight
        return NotImplemented

    def __gt__(self, other: Self) -> bool:
        if isinstance(other, Edge):
            return self.weight > other.weight
        return NotImplemented


def construct_graph(edges: [Edge]) -> Graph:
    result = {}
    for edge in edges:
        if edge.from_vertex not in result:
            result[edge.from_vertex] = {}

        if edge.to_vertex not in result:
            result[edge.to_vertex] = {}

        result[edge.from_vertex][edge.to_vertex] = edge.weight
        result[edge.to_vertex][edge.from_vertex] = edge.weight

    return result


class PrismAlgorithm:
    def __init__(self, graph: Graph):
        self.__mst = self.__calculate_mst(graph)

    def __calculate_mst(self, graph: Graph) -> Graph:
        initial_vertex = next(iter(graph.keys()))
        heap = heapdict()
        heap[initial_vertex] = Edge(initial_vertex, initial_vertex, 0)
        explored = set()
        mst_edges = []

        while len(heap) > 0:
            next_vertex, edge = heap.popitem()
            if next_vertex in explored:
                continue
            explored.add(next_vertex)
            mst_edges.append(edge)
            edges_of_vertex = graph[next_vertex]
            for to_vertex, weight in edges_of_vertex.items():
                if to_vertex not in explored and (to_vertex not in heap or heap[to_vertex].weight > weight):
                    heap[to_vertex] = Edge(next_vertex, to_vertex, weight)

        self.__mst_edges = mst_edges[1:]    # remove first virtual edge

        return construct_graph(self.__mst_edges)

    def get_mst_cost(self) -> int:
        result = 0
        for edge in self.__mst_edges:
            result += edge.weight

        return result

    def get_mst_edges(self):
        return self.__mst_edges
