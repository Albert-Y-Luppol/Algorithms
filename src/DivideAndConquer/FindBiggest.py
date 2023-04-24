# You are a given a unimodal array of n distinct elements, meaning that its entries are in increasing order up until its maximum element, after which its
# elements are in decreasing order. Give an algorithm to compute the maximum element that runs in O(log n) time.

from typing import List


class FindBiggest:
    @staticmethod
    def unimodal(inputArr: List[int]) -> int:
        elements = len(inputArr)

        if elements == 1:
            return inputArr[0]

        if elements == 2:
            return inputArr[0] if inputArr[0] > inputArr[1] else inputArr[1]

        middleIndex = len(inputArr) // 2

        if inputArr[middleIndex] > inputArr[middleIndex + 1] and inputArr[middleIndex] > inputArr[middleIndex - 1]:
            return inputArr[middleIndex];

        return FindBiggest.unimodal(inputArr[middleIndex + 1::]) \
            if inputArr[middleIndex + 1] > inputArr[middleIndex - 1] \
            else FindBiggest.unimodal(inputArr[:middleIndex:])

