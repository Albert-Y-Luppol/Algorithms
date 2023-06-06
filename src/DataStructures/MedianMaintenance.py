from src.DataStructures.Heap import Heap


class MedianMaintenance:
    def __init__(self):
        self.__min_heap = Heap(lambda a, b: a < b)
        self.__max_heap = Heap(lambda a, b: a > b)

    def add(self, n: int) -> None:
        if len(self.__max_heap) == 0:
            self.__max_heap.add(n)
        elif n > self.__max_heap.peak():
            self.__min_heap.add(n)
        else:
            self.__max_heap.add(n)

        self.__balance_heaps()

    def __balance_heaps(self):
        min_h_len = len(self.__min_heap)
        max_h_len = len(self.__max_heap)

        while min_h_len > max_h_len or (max_h_len - min_h_len) > 1:
            if min_h_len > max_h_len:
                smallest_from_large = self.__min_heap.pop()
                self.__max_heap.add(smallest_from_large)
            else:
                biggest_from_small = self.__max_heap.pop()
                self.__min_heap.add(biggest_from_small)

            min_h_len = len(self.__min_heap)
            max_h_len = len(self.__max_heap)

    def median(self) -> int:
        return self.__max_heap.peak()

    def items(self):
        return [self.__max_heap.items(), self.__min_heap.items()]
