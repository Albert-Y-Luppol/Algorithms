import unittest

from src.DivideAndConquer.IntegerMultiplication import IntegerMultiplicator


class IntegerMultiplicationTest(unittest.TestCase):
    def test_School_Algorithm_0(self):
        self.assertEqual(IntegerMultiplicator.schoolMultiplication(3, 5), 3 * 5)

    def test_School_Algorithm_1(self):
        self.assertEqual(IntegerMultiplicator.schoolMultiplication(12, 15), 12 * 15)

    def test_School_Algorithm_2(self):
        self.assertEqual(IntegerMultiplicator.schoolMultiplication(432, 53), 432 * 53)

    def test_School_Algorithm_3(self):
        self.assertEqual(IntegerMultiplicator.schoolMultiplication(45343, 532), 45343 * 532)

    def test_School_Algorithm_4(self):
        self.assertEqual(IntegerMultiplicator.schoolMultiplication(333, 2222), 333 * 2222)

    def test_Recursive_Algorithm_0(self):
        self.assertEqual(IntegerMultiplicator.recursiveAlgorithm(22, 11), 22 * 11)

    def test_Recursive_Algorithm_1(self):
        self.assertEqual(IntegerMultiplicator.recursiveAlgorithm(1234, 5678), 1234 * 5678)

    def test_Recursive_Algorithm_2(self):
        self.assertEqual(
            format(IntegerMultiplicator.recursiveAlgorithm(3141592653589793, 2718281828459045), ".0f"),
            format(3141592653589793 * 2718281828459045, ".0f"),
        )

    def test_Karatsuba_Algorithm_0(self):
        self.assertEqual(IntegerMultiplicator.karatsubaAlgorithm(22, 11), 22 * 11)

    def test_Karatsuba_Algorithm_1(self):
        self.assertEqual(IntegerMultiplicator.karatsubaAlgorithm(1234, 5678), 1234 * 5678)

    def test_Karatsuba_Algorithm_2(self):
        self.assertEqual(IntegerMultiplicator.karatsubaAlgorithm(31415926, 27182818), 31415926 * 27182818)


if __name__ == '__main__':
    unittest.main()
