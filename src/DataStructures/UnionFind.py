from typing import List, Any, Union, Dict, Protocol


class INode(Protocol):
    @property
    def key(self) -> Union[str, int]:
        pass

    @property
    def value(self) -> Any:
        pass


class UnionFindNode:
    def __init__(self, node: INode):
        self.value = node
        self.rank = 0
        self.leader = node.key
        self.key = node.key

    def __str__(self):
        return f'key = {self.key}; value = {self.value}; rank = {self.rank}; leader = {self.leader}'


class UnionFind:
    def __init__(self, nodes_list: List[INode]):
        nodes = {}
        for node in nodes_list:
            nodes[node.key] = UnionFindNode(node)

        self.__nodes: Dict[Union[str, int], UnionFindNode] = nodes

    def find(self, key: Union[str, int]) -> Union[str, int]:
        node = self.__nodes[key]
        leader, visited_nodes = node.leader, [node]    # path compression

        while node.key != leader:
            node = self.__nodes[leader]
            leader = node.leader
            visited_nodes.append(node)

        for visited_node in visited_nodes:  # path compression
            visited_node.leader = leader

        return leader

    def union(self, key1: Union[int, str], key2: Union[int, str]) -> None:
        node1 = self.__nodes[self.find(key1)]
        node2 = self.__nodes[self.find(key2)]

        if node1.key == node2.key:
            return  # already in one group

        if node1.rank > node2.rank:
            node2.leader = node1.key
        elif node2.rank > node1.rank:
            node1.leader = node2.key
        else:
            node2.leader = node1.key
            node1.rank += 1

    def __str__(self):
        result = ""
        for node in self.__nodes.values():
            result += str(node) + "\n"
        return result




