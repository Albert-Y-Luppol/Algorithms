from typing import Tuple, Union
from typing import TypeVar, Callable

T = TypeVar('T')
K = Union[str, int]


class LinkedListNode:
    def __init__(self, key: K, value: T, next_node=None):
        self.value = value
        self.key = key
        self.next = next_node


class LinkedList:
    def __init__(self, initial_values: [Tuple[K, T]] = None, allow_duplicates=False):
        self.head = None
        self.allow_duplicates = allow_duplicates
        for key, value in initial_values if initial_values is not None else []:
            self[key] = value

    def __getitem__(self, key: K) -> T:
        current_node = self.head
        while current_node is not None:
            if current_node.key == key:
                return current_node.value
            current_node = current_node.next
        raise KeyError(key)

    def __setitem__(self, key: K, value: T):
        if self.head is None:
            self.head = LinkedListNode(key, value)
            return

        last_node = self.head
        current_node = self.head.next
        while current_node is not None:
            if self.allow_duplicates and current_node.key == key:
                current_node.value = value
                return

            last_node = current_node
            current_node = current_node.next

        last_node.next = LinkedListNode(key, value)

    def __delitem__(self, key: K):
        current_node = self.head
        previous_node = None
        while current_node is not None:
            if current_node.key == key:
                if previous_node is None:
                    self.head = current_node.next
                else:
                    previous_node.next = current_node.next
                return
            previous_node = current_node
            current_node = current_node.next
        raise KeyError(key)

    def __iter__(self):
        current_node = self.head
        while current_node is not None:
            yield current_node.key, current_node.value
            current_node = current_node.next

    def __len__(self):
        count = 0
        current_node = self.head
        while current_node is not None:
            count += 1
            current_node = current_node.next
        return count

    def __repr__(self):
        return f"LinkedList({[item for item in self]})"

    def __str__(self):
        return f"LinkedList({[item for item in self]})"

    def __contains__(self, key: K):
        current_node = self.head
        while current_node is not None:
            if current_node.key == key:
                return True
            current_node = current_node.next
        return False

    def __get_last_node(self):
        if self.head is None:
            return None

        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        return current_node


class HashTable:
    def __init__(self, hash_function: Callable[[K, int], int], size=101, initial_values=None, allow_duplicates=False):
        self.hash_function = hash_function
        self.size = size
        self.buckets = [LinkedList(allow_duplicates=allow_duplicates) for _ in range(size)]
        if initial_values is not None:
            for key, value in initial_values:
                self[key] = value

    def __setitem__(self, key, value):
        index = self.__get_bucket_index(key)
        llist = self.buckets[index]
        llist[key] = value

    def __getitem__(self, key):
        index = self.__get_bucket_index(key)
        llist = self.buckets[index]
        return llist[key]

    def __delitem__(self, key):
        index = self.__get_bucket_index(key)
        llist = self.buckets[index]
        del llist[key]

    def __contains__(self, key):
        index = self.__get_bucket_index(key)
        llist = self.buckets[index]
        return key in llist

    def __len__(self):
        count = 0
        for llist in self.buckets:
            count += len(llist)
        return count

    def __repr__(self):
        list_str = ',\n\t'.join([str(item) for item in self.buckets])
        return f"HashTable([\n\t{list_str}\n])"

    def __str__(self):
        list_str = ',\n\t'.join([str(item) for item in self.buckets])
        return f"HashTable([\n\t{list_str}\n])"

    def __iter__(self):
        for llist in self.buckets:
            for key, value in llist:
                yield key, value

    def __get_bucket_index(self, key):
        """
            Returns the index of the bucket where the key is stored
            :param key:
            :return:
            :raise IndexError: if the index is greater than the size of the hash table
        """

        index = self.hash_function(key, self.size)
        if index > self.size - 1 or index < 0:
            raise IndexError(f"Hash function returned an bucket index greater than the size of the hash table, key = {key}, "
                             f"index = {index}")
        return index
