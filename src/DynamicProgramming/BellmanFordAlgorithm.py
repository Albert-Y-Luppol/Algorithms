from src.helpers.types import AdjacencyList


class BellmanFordAlgorithm:
    def __init__(self, graph: AdjacencyList, initial_vertex: int):
        self.has_negative_cycle = False
        v_num = len(graph)
        last_cost_memo = {}
        parent_vertex = {}

        for v in graph.keys():
            last_cost_memo[v] = float('inf') if v != initial_vertex else 0
            parent_vertex[v] = None

        for i in range(v_num + 1):
            current_cost_memo = {}
            is_updated = False

            for tail, path_cost in last_cost_memo.items():
                if tail not in current_cost_memo:
                    current_cost_memo[tail] = path_cost

                if path_cost < float('inf'):    # there is a path to this vertex
                    edges = graph[tail].items()
                    for head, edge_cost in edges:
                        if head not in current_cost_memo:   # wasn't reached yet
                            if last_cost_memo[head] > last_cost_memo[tail] + edge_cost:     # found shorter path
                                is_updated = True
                                current_cost_memo[head] = last_cost_memo[tail] + edge_cost
                                parent_vertex[head] = tail
                            else:   # shortest path stays the same
                                current_cost_memo[head] = last_cost_memo[head]
                        else:                               # was reached from another vertex in same iteration of i
                            if current_cost_memo[head] > last_cost_memo[tail] + edge_cost:     # found new shortest path
                                is_updated = True
                                current_cost_memo[head] = last_cost_memo[tail] + edge_cost
                                parent_vertex[head] = tail

            last_cost_memo = current_cost_memo
            if not is_updated:  # early break
                break
            else:
                if i == v_num:  # negative cycle detected
                    self.has_negative_cycle = True

        self.parent_vertex = parent_vertex
        self.vertex_distances = last_cost_memo

    def path_length_to(self, vertex: int) -> int:
        return self.vertex_distances[vertex] if vertex in self.vertex_distances else None

    def path_to(self, vertex: int) -> [int]:
        path = []
        parent_vertex = vertex
        while parent_vertex is not None:
            path.append(parent_vertex)
            parent_vertex = self.parent_vertex[parent_vertex]

        path.reverse()
        return path
