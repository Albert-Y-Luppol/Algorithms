import math
import copy
import random
from typing import Dict, List
from functools import singledispatch
from Graphs.GraphUtils import GraphUtils


class KargerAlgorithm:
    @singledispatch
    def __get_min_cut_overload(graph: Dict[int, List[int]]) -> int:
        return KargerAlgorithm.__getMinCut(graph)

    @__get_min_cut_overload.register(str)
    def _(graph_str: str):
        graph = GraphUtils.strToAdjacencyList(graph_str)
        return KargerAlgorithm.__getMinCut(graph)

    getMinCut = staticmethod(__get_min_cut_overload)

    @staticmethod
    def __getMinCut(graph: Dict[int, List[int]]) -> int:
        node_keys = list(graph.keys())
        amount_of_nodes = len(node_keys)
        amount_of_counts = math.ceil(amount_of_nodes ** 2 * math.log(amount_of_nodes))
        min_cut = len(graph[node_keys[0]])

        print(amount_of_counts)

        while amount_of_counts > 0:
            random_cut = KargerAlgorithm.__getRandomCut(graph)
            min_cut = min(min_cut, random_cut)
            amount_of_counts -= 1

        return min_cut

    @staticmethod
    def __getRandomCut(graph_input: Dict[int, List[int]]) -> int:
        graph = copy.deepcopy(graph_input)
        amount_of_nodes = len(graph.keys())

        while amount_of_nodes > 2:
            graph = KargerAlgorithm.__contractRandomVertex(graph)
            amount_of_nodes -= 1

        return len((graph.popitem())[1])

    @staticmethod
    def __contractRandomVertex(graph: Dict[int, List[int]]) -> Dict[int, List[int]]:
        nodes = list(graph.keys())
        contract_from = random.choice(nodes)
        contract_to = random.choice(graph[contract_from])
        contracting_node = graph.pop(contract_from)

        for end_node in contracting_node:
            graph[end_node] = [contract_to if n == contract_from else n for n in graph[end_node]]

        graph[contract_to] = [n for n in graph[contract_to] + contracting_node if n != contract_to]
        return graph
