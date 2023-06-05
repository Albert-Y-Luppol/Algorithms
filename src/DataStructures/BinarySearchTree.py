from typing import TypeVar, Callable, Union, List

T = TypeVar('T')


class BinarySearchTree:
    class Node:
        key: int
        value: T
        subtree_size = 1
        parent: 'BinarySearchTree.Node' = None
        left: 'BinarySearchTree.Node' = None
        right: 'BinarySearchTree.Node' = None
        is_left: bool = None

        def __init__(self, key: int, value: T):
            self.key = key
            self.value = value

        def __gt__(self, other: Union[int, 'BinarySearchTree.Node']) -> bool:
            return self.key > other

        def __lt__(self, other: Union[int, 'BinarySearchTree.Node']) -> bool:
            return self.key < other

        def __ge__(self, other: Union[int, 'BinarySearchTree.Node']) -> bool:
            return self.key >= other

        def __le__(self, other: Union[int, 'BinarySearchTree.Node']) -> bool:
            return self.key <= other

        def __eq__(self, other: Union[int, 'BinarySearchTree.Node']) -> bool:
            return self.key == other

        def __repr__(self):
            return f'key = {self.key}; value = {self.value}; subtree_size = {self.subtree_size} \n ' \
                   f'\tparent = {None if self.parent is None else self.parent.key}; ' \
                   f'\tleft = {None if self.left is None else self.left.key}; ' \
                   f'\tright = {None if self.right is None else self.right.key}'

        def set_left(self, node: 'BinarySearchTree.Node'):
            self.left = node
            node.parent = self
            node.is_left = True

        def set_right(self, node: 'BinarySearchTree.Node'):
            self.right = node
            node.parent = self
            node.is_left = False

    __root: Union[Node, None] = None

    def __init__(self, key_fn: Callable[[T], int],  initial_nodes: [T] = None):
        if initial_nodes is None:
            initial_nodes = []

        self.__get_key = key_fn

        for node in initial_nodes:
            self.add(node)

    def __repr__(self):
        if self.__root is None:
            return 'None'

        lines, *_ = self.__display_aux(self.__root)
        return '\n'.join(lines)

    def add(self, init_obj: T) -> None:
        key = self.__get_key(init_obj)
        node = self.Node(key, init_obj)

        if self.__root is None:
            self.__root = node
        else:
            self.__insert_node(node)

    def remove(self, key: int) -> None:
        node_to_remove = self.__get_node(key)

        if node_to_remove is None:
            return

        self.__remove_node(node_to_remove)

    def get(self, key: int) -> Union[T, None]:
        node = self.__get_node(key)
        if node is None:
            return node
        else:
            return node.value

    def get_key(self, node_value: T) -> int:
        return self.__get_key(node_value)

    def rank(self, key: int) -> Union[int, None]:
        node = self.__get_node(key)
        if node is None:
            return None

        rank = 1
        if node.left is not None:
            rank += node.left.subtree_size

        current = node
        while current.parent is not None:
            if not current.is_left:
                rank += current.parent.subtree_size - current.subtree_size

            current = current.parent

        return rank


    @staticmethod
    def __get_predecessor(current_node: 'BinarySearchTree.Node') -> Union['BinarySearchTree.Node', None]:
        if current_node.left is not None:
            result = current_node.left
            while result.right is not None:
                result = result.right
        else:
            result = None
            current = current_node
            while current.parent is not None:
                if not current.is_left:
                    result = current.parent
                    break

                current = current.parent

        return result

    @staticmethod
    def __get_successor(current_node: 'BinarySearchTree.Node') -> Union['BinarySearchTree.Node', None]:
        if current_node.right is not None:
            result = current_node.right
            while result.left is not None:
                result = result.left
        else:
            result = None
            current = current_node
            while current.parent is not None:
                if current.is_left:
                    result = current.parent
                    break

                current = current.parent

        return result

    def __get_node(self, key: int) -> Union['BinarySearchTree.Node', None]:
        current = self.__root
        while current is not None and key != current:
            if key < current:
                current = current.left
            else:
                current = current.right

        return current

    def __insert_node(self, node: Node, current=None) -> None:
        if current is None:
            current = self.__root

        current.subtree_size += 1

        if node < current:
            if current.left is None:
                current.set_left(node)
            else:
                self.__insert_node(node, current.left)
        else:
            if current.right is None:
                current.set_right(node)
            else:
                self.__insert_node(node, current.right)

    def __remove_node(self, node_to_remove: Node) -> None:
        is_root = self.__root == node_to_remove

        if node_to_remove.subtree_size == 1:    # means node without children
            if is_root:
                self.__root = None
            else:
                setattr(node_to_remove.parent, 'left', None) \
                    if node_to_remove.is_left \
                    else setattr(node_to_remove.parent, 'right', None)
                self.__modify_subtree_size(node_to_remove.parent, -1)
        elif node_to_remove.left is None or node_to_remove.right is None:   # node with one child
            child = node_to_remove.left if node_to_remove.left is not None else node_to_remove.right
            if is_root:
                self.__root = child
                child.parent = None
            else:
                setattr(node_to_remove.parent, 'left', child) \
                    if node_to_remove.is_left \
                    else setattr(node_to_remove.parent, 'right', child)
                child.parent = node_to_remove.parent
                self.__modify_subtree_size(node_to_remove.parent, -1)
        else:   # 2 children, no matter root or not
            child = node_to_remove.left
            while child.right is not None:
                child = child.right
            self.__swap_nodes(node_to_remove, child)
            self.__remove_node(child)

    @staticmethod
    def __swap_nodes(a: Node, b: Node) -> None:
        memo = a.key
        a.key = b.key
        b.key = memo
        memo = a.value
        a.value = b.value
        b.value = memo

    @staticmethod
    def __modify_subtree_size(node: Node, value: int) -> None:
        while node is not None:
            node.subtree_size += value
            node = node.parent

    def __display_aux(self, node: Node):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if node.right is None and node.left is None:
            line = '%s' % node.key
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if node.right is None:
            lines, n, p, x = self.__display_aux(node.left)
            s = '%s' % node.key
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if node.left is None:
            lines, n, p, x = self.__display_aux(node.right)
            s = '%s' % node.key
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.__display_aux(node.left)
        right, m, q, y = self.__display_aux(node.right)
        s = '%s' % node.key
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2
