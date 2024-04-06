import numbers
from typing import Dict, TypeVar

V = TypeVar('V', bound=int)
W = TypeVar('W', bound=numbers.Number)


AdjacencyList = Dict[V, Dict[V, W]]
