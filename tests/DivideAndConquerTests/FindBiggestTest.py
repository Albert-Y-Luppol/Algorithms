import unittest

from src.DvideAndConquer.FindBiggest import FindBiggest


class FindBiggestTest(unittest.TestCase):
    def test_standard_1(self):
        plain_data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1]
        fn_input = list(plain_data)
        fn_output = 7

        self.assertEqual(FindBiggest.unimodal(fn_input), fn_output)

    def test_standard_2(self):
        plain_data = [0, 1]
        fn_input = list(plain_data)
        fn_output = 1

        self.assertEqual(FindBiggest.unimodal(fn_input), fn_output)

    def test_standard_3(self):
        plain_data = [2]
        fn_input = list(plain_data)
        fn_output = 2

        self.assertEqual(FindBiggest.unimodal(fn_input), fn_output)

    def test_standard_4(self):
        plain_data = [1, 2, 3, 4, 5, 6]
        fn_input = list(plain_data)
        fn_output = 6

        self.assertEqual(FindBiggest.unimodal(fn_input), fn_output)


if __name__ == '__main__':
    unittest.main()
