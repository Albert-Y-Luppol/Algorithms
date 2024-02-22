import unittest
from DataStructures.UnionFind import UnionFind


class Node:
    def __init__(self, key):
        self.key = key
        self.value = key


class UnionFindTest(unittest.TestCase):
    def test1(self):
        nodes = [Node(n) for n in [1, 2, 3, 4, 5, 6]]
        uf = UnionFind(nodes)
        uf.union(1, 2)  # 1 rank 1
        uf.union(3, 4)  # 3 rank 1
        uf.union(5, 6)  # 5 rank 1
        uf.union(4, 5)  # 3 rank 2
        uf.union(2, 3)

        for n in nodes:
            uf.find(n.key)

        print(uf)

        for node in nodes:
            self.assertEqual(uf.find(node.key), 3)

        self.assertEqual(str(uf.clusters), str({3}))


