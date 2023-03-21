import random
from typing import List


class QuickSort:
    @staticmethod
    def sort(inputArr: List[int]) -> List[int]:
        result = inputArr.copy()
        QuickSort.__sort(result, 0, len(inputArr) - 1)
        return result

    @staticmethod
    def __sort(list: List[int], start: int, end: int) -> None:
        if end - start < 1:
            return

        median_index = QuickSort.__choosePivotIndex(list, start, end)
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
        QuickSort.__sort(list, start, partition_boundary - 1)
        QuickSort.__sort(list, partition_boundary + 1, end)

    @staticmethod
    def __choosePivotIndex(list: List[int], start: int, end: int) -> int:
        return random.randint(start, end)
