import re
import math
from src.helpers.types import AdjacencyList
from typing import Tuple
import numbers
import heapdict
from src.helpers.monitoring import print_monitor


def str_to_adjacency_list(input_str: str) -> AdjacencyList:
    text_rows = input_str.strip().split('\n')
    edge_rows = text_rows[1:]
    edges = [re.split(r'\s+', row.strip()) for row in edge_rows]
    result: AdjacencyList = {}
    for edge in edges:
        tail, head, weight = list(map(lambda v: int(v), edge))
        if tail not in result:
            result[tail] = {}

        if head not in result:
            result[head] = {}

        if head in result[tail]:
            result[tail][head] = min(result[tail][head], weight)
        else:
            result[tail][head] = weight
    return result


def points_to_graph_2d(points: [Tuple[numbers.Number, numbers.Number]]) -> AdjacencyList[int, float]:
    n = len(points)     # amount
    graph: AdjacencyList[int, float] = {}
    for i in range(n):
        graph[i] = {}

    for p1 in range(n):
        for p2 in range(p1 + 1, n):
            x1, y1 = points[p1]
            x2, y2 = points[p2]
            edge = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
            graph[p1][p2] = edge
            graph[p2][p1] = edge

    return graph
