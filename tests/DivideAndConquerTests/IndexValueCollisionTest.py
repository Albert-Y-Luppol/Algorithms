import unittest

from src.DivideAndConquer.IndexValueCollision import indexValueCollision


class IndexValueCollisionTest(unittest.TestCase):
    def test_standard_1(self):
        fn_input = [1, 2, 3]
        exp_output = False

        self.assertEqual(exp_output, indexValueCollision(fn_input))

    def test_standard_2(self):
        fn_input = [0, 2, 3]
        exp_output = True

        self.assertEqual(exp_output, indexValueCollision(fn_input))

    def test_standard_3(self):
        fn_input = [-3, -1, 0, 3, 10, 20]
        exp_output = True

        self.assertEqual(exp_output, indexValueCollision(fn_input))

    def test_standard_4(self):
        fn_input = [-3, -1, 0, 2, 10, 20]
        exp_output = False

        self.assertEqual(exp_output, indexValueCollision(fn_input))


if __name__ == '__main__':
    unittest.main()
