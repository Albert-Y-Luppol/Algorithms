from typing import Tuple
import math
import random
from src.helpers.monitoring import print_progress_bar
import networkx as nx


class PapadimitriousAlgorithm:
    @staticmethod
    def is_assignment_available(booleans_number: int, clauses: [Tuple[int, int]], loader=False) -> bool:
        loader_i = 0
        loader_total = int(math.log2(booleans_number)) * 2 * booleans_number ** 2
        for _ in range(int(math.log2(booleans_number))):
            assignment = []
            for _ in range(booleans_number):
                assignment.append(random.choice([True, False]))

            for _ in range(2 * booleans_number ** 2):
                unsatisfied_clauses = []
                for x_i, x_j in clauses:
                    i = abs(x_i) - 1
                    j = abs(x_j) - 1
                    i_b = True if x_i > 0 else False
                    j_b = True if x_j > 0 else False

                    if assignment[i] != i_b and assignment[j] != j_b:
                        unsatisfied_clauses.append((x_i, x_j))

                if len(unsatisfied_clauses) == 0:
                    return True
                else:
                    clause = random.choice(unsatisfied_clauses)
                    flip_var = random.choice(clause)
                    var_i = abs(flip_var) - 1
                    assignment[var_i] = not assignment[var_i]

                if loader:
                    loader_i += 1
                    print_progress_bar(loader_i, loader_total)

        return False


class StronglyConnectedComponents:
    @staticmethod
    def is_assignment_available(clauses: [Tuple[int, int]], loader=False) -> bool:
        edges = []
        for a, b in clauses:
            edges.append((a * -1, b))
            edges.append((b * -1, a))

        sccs = StronglyConnectedComponents.__get_scc(edges)

        i = 0
        total = len(sccs)

        for scc in sccs:
            forbidden = set()
            for v in scc:
                if v in forbidden:
                    return False
                forbidden.add(v * -1)

            if loader:
                i += 1
                print_progress_bar(i, total)

        return True

    @staticmethod
    def __get_scc(edges):
        graph = nx.DiGraph()
        graph.add_edges_from(edges)
        return list(nx.strongly_connected_components(graph))
