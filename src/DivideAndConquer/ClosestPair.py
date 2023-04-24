from typing import List, TypeVar, Generic
from dataclasses import dataclass
import math

T = TypeVar('T')


@dataclass
class Point:
    x: int
    y: int


@dataclass
class Pair(Generic[T]):
    first: T
    second: T


class ClosestPair:
    @staticmethod
    def run(points: List[Point]) -> Pair[Point]:
        Px = points.copy()
        Px.sort(key=lambda p: p.x)  # O(nlog(n))
        Py = points.copy()
        Py.sort(key=lambda p: p.y)  # O(nlog(n))

        return ClosestPair.__getClosestPair(Px, Py)

    @staticmethod
    def __getClosestPair(Px: List[Point], Py: List[Point]) -> Pair[Point]:
        if (len(Px) == 1 and len(Py) == 1):
            return Pair[Point](Px[0], Py[0])

        Lx = Px[:math.floor(len(Px) / 2):]
        Rx = Px[math.floor(len(Px) / 2)::]
        Ly = Py[:math.floor(len(Py) / 2):]
        Ry = Py[math.floor(len(Py) / 2)::]

        leftPair = ClosestPair.__getClosestPair(Lx, Ly)
        rightPair = ClosestPair.__getClosestPair(Rx, Ry)

        leftPairDelta = ClosestPair.__getDistanceBetweenPoints(leftPair.first, leftPair.second)
        rightPairDelta = ClosestPair.__getDistanceBetweenPoints(rightPair.first, rightPair.second)

        delta = min(leftPairDelta, rightPairDelta)

        pairInSplit = ClosestPair.__getClosestSplitPair(Px, Py, delta)

        if pairInSplit is None:
            return rightPair if rightPairDelta > leftPairDelta else leftPair
        else:
            return pairInSplit


    @staticmethod
    def __getClosestSplitPair(Px: List[Point], Py: List[Point], delta: int) -> Pair[Point]:
        middleXPoint = Px[math.floor(len(Px) / 2)]
        minX = middleXPoint.x - delta
        maxX = middleXPoint.x + delta

        minDelta = delta
        result = None

        Sy = list(filter(lambda p: maxX > p.x > minX, Py))

        i = 0
        while i < len(Sy) - 1:
            j = 1
            while j < 8 and i + j < len(Sy):
                d = ClosestPair.__getDistanceBetweenPoints(Sy[i], Sy[i + j])
                if d < minDelta:
                    minDelta = d
                    result = Pair[Point](Sy[i], Sy[i + j])

                j+= 1
            i+= 1

        return result


    @staticmethod
    def __getDistanceBetweenPoints(A: Point, B: Point) -> int:
        return math.sqrt(pow(B.x - A.x, 2) + pow(B.y - A.y, 2))