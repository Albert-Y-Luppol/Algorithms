# Kruskal's MST based algorithm

from typing import Set, List
import heapq
from DataStructures.UnionFind import UnionFind

Key = int | str


class Vertex:
    def __init__(self, key, value = None):
        self.key = key
        self.value = value if value is not None else key

    def __str__(self):
        return f"Vertex(key={self.key}, value={self.value})"


class Edge:
    def __init__(self, vertex1: Key, vertex2: Key, distance: int):
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.distance = distance

    def __str__(self):
        return f"Edge(vertex1={self.vertex1}, vertex2={self.vertex2}, distance={self.distance})"

    def __lt__(self, other):
        return self.distance < other.distance

    def __le__(self, other):
        return self.distance <= other.distance

    def __eq__(self, other):
        if not isinstance(other, Edge):
            return NotImplemented
        return self.distance == other.distance

    def __ne__(self, other):
        if not isinstance(other, Edge):
            return NotImplemented
        return self.distance != other.distance

    def __gt__(self, other):
        return self.distance > other.distance

    def __ge__(self, other):
        return self.distance >= other.distance


class ClusteringAlgorithm:
    @staticmethod
    def find_max_spacing_k_clusters(edges: [Edge], clusters_count: int) -> (int, UnionFind):
        edges_heap: List[Edge] = []
        vertices: Set[int] = set()
        for edge in edges:
            heapq.heappush(edges_heap, edge)
            vertices.add(edge.vertex1)
            vertices.add(edge.vertex2)

        union_find = UnionFind([Vertex(vertex) for vertex in vertices])

        max_spacing = 0
        while len(edges_heap) > 0:
            edge = heapq.heappop(edges_heap)
            leader1 = union_find.find(edge.vertex1)
            leader2 = union_find.find(edge.vertex2)
            if len(union_find.clusters) > clusters_count or leader1 == leader2:
                union_find.union(edge.vertex1, edge.vertex2)
                max_spacing = edge.distance

        return max_spacing, union_find

    @staticmethod
    def find_max_clusters_with_min_spacing_by_hamming_distance(vertices: [tuple], max_spacing: int) -> (int, UnionFind):
        uf = UnionFind([Vertex(vertex) for vertex in vertices])
        for i in range(len(vertices) - 1):
            print(i)
            vertex = vertices[i]
            same_cluster_vertices_options = generate_same_cluster_options(vertex, max_spacing)
            for j in range(i + 1, len(vertices)):
                target_vertex = vertices[j]
                if target_vertex in same_cluster_vertices_options:
                    uf.union(vertex, target_vertex)

        return len(uf.clusters), uf


def generate_same_cluster_options(vertex: tuple, level_of_distinctivity: int) -> Set[tuple]:
    result = set()
    vertex_as_list = list(vertex)

    def generate_option_from_index(i: int, level: int):
        nonlocal result
        nonlocal vertex_as_list
        nonlocal vertex

        level -= 1

        for j in range(i + 1, len(vertex)):
            vertex_as_list[j] = not vertex_as_list[j]
            result.add(tuple(vertex_as_list))
            if level > 0:
                generate_option_from_index(j, level)
            vertex_as_list[j] = not vertex_as_list[j]

    generate_option_from_index(-1, level_of_distinctivity)

    return result
