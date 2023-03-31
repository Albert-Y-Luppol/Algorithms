import math


class FibonacciNumbers:
    @staticmethod
    def generateFibonacciSequence(n: int) -> [int]:     # O(n)
        result: [int] = []
        while n >= 1:
            n -= 1
            if len(result) < 2:
                result.append(1)
            else:
                result.append(result[-1] + result[-2])
        return result

    @staticmethod
    def sumFirstNFibonacciNumbers(n: int) -> int:     # O(n)
        numbers = FibonacciNumbers.generateFibonacciSequence(n)
        return sum(numbers)

    @staticmethod
    def lastDigitOfNthFibonacciNumber(n: int) -> int:     # O(n)
        last_digit: int = None
        before_last_digit: int = None
        while n >= 1:
            n -= 1
            if last_digit is None:
                last_digit = 1
            elif before_last_digit is None:
                before_last_digit = last_digit
                last_digit = 1
            else:
                current = (last_digit + before_last_digit) % 10
                before_last_digit = last_digit
                last_digit = current

        return last_digit

    @staticmethod
    def nthFibonacciNumber(n: int) -> int:     # Binet's formula
        phi = (1 + 5**.5) / 2
        psi = (1 - 5**.5) / 2
        return round((phi**n - psi**n) / 5**.5)

    @staticmethod
    def sumOfNthFibonacciNumbers(n: int) -> int:     # Binet's formula
        phi = (1 + 5**.5) / 2
        psi = (1 - 5**.5) / 2
        return round((phi**(n + 2) - psi**(n + 2)) / 5**.5) - 1
