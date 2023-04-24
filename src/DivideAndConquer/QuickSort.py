import random
from typing import List, Callable


class QuickSort:
    @staticmethod
    def sort(inputArr: List[int]) -> List[int]:
        result = inputArr.copy()
        QuickSort.__sort(result, 0, len(inputArr) - 1)
        return result

    @staticmethod
    def __choosePivotIndex(list: List[int], start: int, end: int) -> int:
        return random.randint(start, end)

    @staticmethod
    def __sort(
            list: List[int],
            start: int,
            end: int,
            partition_fn: Callable[[List[int], int, int], int] = __choosePivotIndex,
    ) -> int:
        if end - start < 1:
            return 0

        median_index = partition_fn(list, start, end)
        partition_element = list[median_index]
        list[median_index] = list[start]
        list[start] = partition_element
        partition_boundary = start

        for i in range(start + 1, end + 1):
            if list[i] < partition_element:
                partition_boundary += 1
                temp = list[i]
                list[i] = list[partition_boundary]
                list[partition_boundary] = temp

        list[start] = list[partition_boundary]
        list[partition_boundary] = partition_element

        number_of_comparisons = end - start
        number_of_comparisons += QuickSort.__sort(list, start, partition_boundary - 1, partition_fn)
        number_of_comparisons += QuickSort.__sort(list, partition_boundary + 1, end, partition_fn)
        return number_of_comparisons

    @staticmethod
    def countComparisons(
            inputArr: List[int],
            partition_fn: Callable[[List[int], int, int], int] = __choosePivotIndex,
    ) -> int:
        sortedArr = inputArr.copy()
        result = QuickSort.__sort(sortedArr, 0, len(sortedArr) - 1, partition_fn)
        return result
