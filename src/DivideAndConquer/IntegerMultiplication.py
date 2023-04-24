from math import *


class IntegerMultiplicator:
    @staticmethod
    def schoolMultiplication(a: int, b: int) -> int:
        aArr = list(int(i) for i in str(a))
        bArr = list(int(i) for i in str(b))

        result = 0

        for i, bDigit in enumerate(bArr):
            row = 0
            rowMultiplyer = 10 ** (len(bArr) - i - 1)
            for j, aDigit in enumerate(aArr):
                columnMultiplyer = 10 ** (len(aArr) - 1 - j)
                row += aDigit * bDigit * columnMultiplyer

            result += row * rowMultiplyer

        return result

    @staticmethod
    def recursiveAlgorithm(x: int, y: int) -> int:
        n = lX = len(str(x))
        lY = len(str(y))

        if lX != lY or lX % 2 != 0:
            return x * y

        delimiter = 10 ** (n / 2)

        a = int(x // delimiter)
        b = int(x % delimiter)

        c = int(y // delimiter)
        d = int(y % delimiter)

        return 10 ** n * IntegerMultiplicator.recursiveAlgorithm(a, c) + delimiter \
            * (IntegerMultiplicator.recursiveAlgorithm(a, d) + IntegerMultiplicator.recursiveAlgorithm(b, c)) \
            + IntegerMultiplicator.recursiveAlgorithm(b, d)

    @staticmethod
    def karatsubaAlgorithm(x: int, y: int) -> int:
        if x < 10 or y < 10:
            return x * y

        n = max(len(str(x)), len(str(y)))

        delimiter = 10 ** (n / 2)

        a = int(x // delimiter)
        b = int(x % delimiter)

        c = int(y // delimiter)
        d = int(y % delimiter)

        ac = IntegerMultiplicator.karatsubaAlgorithm(a, c)
        bd = IntegerMultiplicator.karatsubaAlgorithm(b, d)

        abcd = (a + b) * (c + d) - ac - bd

        return int(10 ** n * ac + delimiter * abcd + bd)
