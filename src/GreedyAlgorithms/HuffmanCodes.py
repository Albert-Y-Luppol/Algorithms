import heapq
from typing import Union


class NodeLike:
    def __init__(self, weight: int):
        self.weight = weight

    def __eq__(self, other):
        if not isinstance(other, NodeLike):
            return NotImplemented
        return self.weight == other.weight

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if not isinstance(other, NodeLike):
            return NotImplemented
        return self.weight < other.weight

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other):
        if not isinstance(other, NodeLike):
            return NotImplemented
        return self.weight > other.weight

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)

    def __str__(self):
        return f'NodeLike({self.weight})'


class Leaf(NodeLike):
    def __init__(self, weight, symbol: str = None):
        super().__init__(weight)
        self.symbol = symbol

    def __str__(self):
        return f'Leaf({self.weight if self.symbol is None else self.symbol})'


class Node(NodeLike):
    def __init__(self, left: Union['Node', Leaf], right: Union['Node', Leaf]):
        super().__init__(left.weight + right.weight)
        self.left = left
        self.right = right

    def __str__(self):
        return self._str(0)

    def _str(self, level):
        indent = ' ' * (level * 4)  # Increase the multiplier to increase indentation
        left_str = self.left._str(level + 1) if hasattr(self.left, '_str') else ' ' * ((level + 1) * 4) + str(self.left)
        right_str = self.right._str(level + 1) if hasattr(self.right, '_str') else ' ' * ((level + 1) * 4) + str(self.right)
        return f'{indent}Node({self.weight})\n{left_str}\n{right_str}'


class HoffmanCodes:
    def __init__(self, weights: [int]):
        heap = []
        for w in weights:
            heapq.heappush(heap, Leaf(w))

        while len(heap) > 1:
            right = heapq.heappop(heap)
            left = heapq.heappop(heap)
            heapq.heappush(heap, Node(left, right))

        self.bst = heapq.heappop(heap)

    def get_bst_attributes(self):
        return self._depth(self.bst)

    def _depth(self, node: Node | Leaf) -> (int, int):
        if isinstance(node, Leaf):
            return 0, 0
        else:
            left_min, left_max = self._depth(node.left)
            right_min, right_max = self._depth(node.right)
            return min(left_min, right_min) + 1, max(left_max, right_max) + 1
