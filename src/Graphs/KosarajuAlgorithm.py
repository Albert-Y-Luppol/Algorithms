from typing import Set, Dict, Tuple, FrozenSet

Graph = Dict[int, Tuple[Set[int], Set[int]]]


class KosarajuAlgorithm:
    @staticmethod
    def findStronglyConnectedComponents(graph: Graph, recursively=False) -> FrozenSet[FrozenSet[int]]:
        graph_exploration_order = \
            KosarajuAlgorithm.__orderVertexesByFinishingTimeRecursively(graph, reverse=True) \
            if recursively \
            else KosarajuAlgorithm.__orderVertexesByFinishingTimeIteratively(graph, reverse=True)

        graph_exploration_order.reverse()

        result = set()
        last_sub_graph = set()
        for vertex in graph_exploration_order:
            if vertex in last_sub_graph:
                continue
            current_sub_graph = KosarajuAlgorithm.__dfs(graph, vertex)
            scc = current_sub_graph - last_sub_graph
            result.add(frozenset(scc))
            last_sub_graph |= current_sub_graph

        return frozenset(result)

    @staticmethod
    def constructGraphFromEdgesList(edges: [Tuple[int, int]]) -> Graph:
        graph = dict()
        for edge in edges:
            from_vertex, to_vertex = edge

            for vertex in edge:
                if vertex not in graph:
                    graph[vertex] = (set(), set())

            graph[from_vertex][1].add(to_vertex)
            graph[to_vertex][0].add(from_vertex)

        return graph

    @staticmethod
    def __orderVertexesByFinishingTimeRecursively(
            graph: Graph,
            reverse=False
    ) -> [int]:
        result = []

        for vertex in graph.keys():
            if vertex in result:
                continue
            KosarajuAlgorithm.__orderVertexesByFinishingTimeVertexRoutine(
                graph, vertex, result, reverse=reverse, explored=set(result)
            )
        return result

    @staticmethod
    def __orderVertexesByFinishingTimeVertexRoutine(
            graph: Graph,
            from_vertex: int,
            result: [int],
            explored: Set[int],
            reverse=False,
    ) -> None:
        i = 0 if reverse else 1

        explored.add(from_vertex)

        for next_vertex in graph[from_vertex][i]:
            if next_vertex in explored:
                continue

            KosarajuAlgorithm.__orderVertexesByFinishingTimeVertexRoutine(
                graph, next_vertex, result, explored, reverse
            )

        result.append(from_vertex)

    @staticmethod
    def __orderVertexesByFinishingTimeIteratively(
            graph: Graph,
            reverse=False
    ) -> [int]:
        counter = 0
        result = []
        i = 0 if reverse else 1

        for vertex in graph.keys():
            if vertex in result:
                continue

            edges_stack = [(0, vertex)]
            explored = set(result)

            while len(edges_stack) > 0:
                counter += 1
                previous_vertex, current_vertex = edges_stack.pop()

                if previous_vertex == current_vertex:
                    result.append(current_vertex)
                    continue

                if current_vertex in explored:
                    continue

                explored.add(current_vertex)
                edges_stack.append((current_vertex, current_vertex))

                edges_of_current_vertex = [(current_vertex, next_vertex)
                                           for next_vertex in graph[current_vertex][i]
                                           if next_vertex not in explored]
                edges_stack += edges_of_current_vertex

            print(counter)

        return result

    @staticmethod
    def __dfs(graph: Graph, from_vertex: int) -> Set[int]:
        stack = [from_vertex]
        explored = set()

        while len(stack) > 0:
            current_vertex = stack.pop()
            if current_vertex in explored:
                continue

            explored.add(current_vertex)
            stack.extend(graph[current_vertex][1])

        return explored
