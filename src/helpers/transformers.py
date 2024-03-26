import re
from src.helpers.types import AdjacencyList


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
