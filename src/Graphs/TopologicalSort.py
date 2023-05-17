from typing import Dict, Set
import copy


class TopologicalSort:
    @staticmethod
    def straightForwardAlgorithm(graph_input: Dict[int, Set[int]]) -> [int]:
        """
        :raises Exception: If graph is circular.
        """

        graph = copy.deepcopy(graph_input)
        result = []
        while len(graph) > 0:
            sink_vertices = TopologicalSort.__findSinkVertices(graph)

            if len(sink_vertices) == 0:
                raise Exception('There is no way to order graph with cycle in it!')

            for vertex in sink_vertices:
                result.append(vertex)
                TopologicalSort.__shrinkVertex(graph, vertex)

        result.reverse()
        return result

    @staticmethod
    def dfsAlgorithm(graph: Dict[int, Set[int]]) -> [int]:
        """
        :raises Exception: If graph is circular.
        """

        if TopologicalSort.__isGraphCircular(graph):
            raise Exception('There is no way to order graph with cycle in it!')

        result = []
        explored_vertices = set()

        for cur_vertex in graph.keys():
            if cur_vertex in result:
                continue

            TopologicalSort.__dfsAlgorithms(graph, cur_vertex, result, explored_vertices)

            if len(result) == len(graph):
                break

        result.reverse()
        return result

    @staticmethod
    def __findSinkVertices(graph: Dict[int, Set[int]]) -> Set[int]:
        return {vertex for vertex in graph.keys() if len(graph[vertex]) == 0}

    @staticmethod
    def __shrinkVertex(graph: Dict[int, Set[int]], vertex_to_shrink: int) -> None:
        del graph[vertex_to_shrink]
        for pointers in graph.values():
            if len(pointers) > 0:
                pointers.discard(vertex_to_shrink)

    @staticmethod
    def __dfsAlgorithms(
            graph: Dict[int, Set[int]],
            cur_vertex: int,
            result: [int],
            explored_vertices: Set[int],
    ) -> None:
        explored_vertices.add(cur_vertex)
        for vertex in graph[cur_vertex]:
            if vertex not in explored_vertices:
                TopologicalSort.__dfsAlgorithms(graph, vertex, result, explored_vertices)

        result.append(cur_vertex)

    @staticmethod
    def __circularityValidation(graph_input: Dict[int, Set[int]]) -> None:
        graph = copy.deepcopy(graph_input)
        for vertex in list(graph.keys()):
            is_pointing_to_itself = vertex in graph[vertex]
            if is_pointing_to_itself:
                raise Exception('There is no way to order graph with cycle in it!')

            TopologicalSort.__collapseVertex(graph, vertex)

    @staticmethod
    def __collapseVertex(graph: Dict[int, Set[int]], vertex_to_collapse: int) -> None:
        edges_from_collapsing_vertex = graph.pop(vertex_to_collapse)

        for every_vertex_left in graph.keys():
            is_vertex_pointing_to_collapsing_one = vertex_to_collapse in graph[every_vertex_left]
            if is_vertex_pointing_to_collapsing_one:
                graph[every_vertex_left].remove(vertex_to_collapse)
                graph[every_vertex_left] = graph[every_vertex_left] | edges_from_collapsing_vertex

    @staticmethod
    def __isGraphCircular(
            graph: Dict[int, Set[int]],
    ) -> bool:
        path: Set[int] = set()
        validated: Set[int] = set()

        for vertex in graph.keys():
            if vertex in validated:
                continue
            if len(validated) == len(graph):
                break

            if TopologicalSort.__isGraphCircularFromVertex(graph, vertex, path, validated):
                return True

        return False

    @staticmethod
    def __isGraphCircularFromVertex(
            graph: Dict[int, Set[int]],
            vertex: int,
            path: Set[int],
            validated: Set[int],
    ) -> bool:
        if vertex in path:
            return True

        path.add(vertex)

        for next_vertex in graph[vertex]:
            if next_vertex in validated:
                continue

            if TopologicalSort.__isGraphCircularFromVertex(graph, next_vertex, path, validated):
                return True

        path.remove(vertex)
        validated.add(vertex)
        return False
