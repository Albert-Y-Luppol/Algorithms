from src.DataStructures.BinarySearchTree import BinarySearchTree


class BalancedBinarySearchTree(BinarySearchTree):
    @staticmethod
    def rotate(parent: BinarySearchTree.Node, child: BinarySearchTree.Node) -> None:
        if parent.left != child and parent.right != child:
            raise 'Rotation available only among direct ancestors'

        is_rotate_right = child.is_left

        p = parent.parent
        subtree = child.left if is_rotate_right else child.left    # parent < subtree < child

        child.parent = p
        parent.parent = child
        setattr(parent, 'left', subtree) if is_rotate_right else setattr(parent, 'right', subtree)

        if subtree is not None:
            subtree.is_left = not subtree.is_left

        memo = parent.is_left
        parent.is_left = not child.is_left
        child.is_left = memo

        child.subtree_size = parent.subtree_size
        parent.subtree_size = 0 if parent.left is None else parent.left.subtree_size \
            + 0 if parent.right is None else parent.right.subtree_size \
            + 1


