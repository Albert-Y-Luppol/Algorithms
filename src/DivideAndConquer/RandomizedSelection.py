import random

class RandomizeSelection:
    @staticmethod
    def select_ith_element(n_arr: [int], search_i: int) -> int:
        """
        :param n_arr: n length list of integers
        :param search_i: 1 - based index of element you need of sorted n_arr list
        :return: value of i-th element in sorted list.

        Takes O(n) time and use O(1) additional memory
        """
        return RandomizeSelection.__select_ith_element(n_arr, search_i - 1, 0, len(n_arr) - 1)

    @staticmethod
    def __select_ith_element(n_arr: [int], search_i: int, start_i: int, end_i: int) -> int:
        if start_i == end_i:
            return n_arr[search_i + start_i]

        random_pivot = random.randint(start_i, end_i)
        pivot_i = RandomizeSelection.__single_sorting_activity(n_arr, start_i, end_i, random_pivot)

        if pivot_i == (search_i + start_i):
            return n_arr[pivot_i]
        elif pivot_i > (search_i + start_i):
            return RandomizeSelection.__select_ith_element(n_arr, search_i, start_i, pivot_i - 1)
        else:
            return RandomizeSelection.__select_ith_element(n_arr, search_i + start_i - pivot_i - 1, pivot_i + 1, end_i)

    @staticmethod
    def __single_sorting_activity(n_arr: [int], start_i: int, end_i: int, pivot_index: int) -> int:
        """
        Returns index of pivot element in sorted n_arr and mutate n_arr input as one iteration of quick sort algorithm.
        Use O(n) time and O(1) memory
        """
        memo = n_arr[pivot_index]
        n_arr[pivot_index] = n_arr[start_i]
        n_arr[start_i] = memo
        i = start_i
        for j in range(start_i + 1, end_i + 1):
            if n_arr[i] > n_arr[j]:
                memo = n_arr[j]
                n_arr[j] = n_arr[i + 1]
                n_arr[i + 1] = n_arr[i]
                n_arr[i] = memo
                i += 1

        return i
