class EuclideanAlgorithm:
    @staticmethod
    def greatestCommonDivisor(a: int, b: int) -> [int]:  # O(n)
        if a == 0 or b == 0:
            return a if a > b else b

        x, y = (a, b) if a > b else (b, a)
        remainder: int = None
        while remainder != 0:
            remainder = x % y
            x = y
            y = remainder

        return x

    @staticmethod
    def leastCommonDivisor(a: int, b: int) -> [int]:  # O(n)
        if a == 0 or b == 0:
            return a if a > b else b
        gcd = EuclideanAlgorithm.greatestCommonDivisor(a, b)
        return a * b // gcd
