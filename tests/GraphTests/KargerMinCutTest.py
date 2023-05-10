import unittest
from Graphs.KargerAlgorithm import KargerAlgorithm


class KargerAlgorithmTest(unittest.TestCase):
    # def test_contract_random_node_1(self):
    #     input_str = {1: [2, 3], 2: [1, 3], 3: [1, 2]}
    #     result = KargerAlgorithm.contractRandomNode(input_str)
    #     print(result)
    #     expected_output = 2
    #     self.assertEqual(expected_output, len(list(result.keys())))

    def test_get_min_cut_1(self):
        input_str = {1: [2], 2: [3, 1], 3: [2]}
        expected_output = 1
        self.assertEqual(expected_output, KargerAlgorithm.getMinCut(input_str))

    def test_get_min_cut_2(self):
        input_str = '1 2\n2 3\n3 1'
        expected_output = 1
        self.assertEqual(expected_output, KargerAlgorithm.getMinCut(input_str))

    def test_get_min_cut_3(self):
        input_str = '1 2 3 4 5\n2 1 3 4 5\n3 1 2 4 5\n4 1 2 3 5\n5 1 2 3 4'
        expected_output = 4
        self.assertEqual(expected_output, KargerAlgorithm.getMinCut(input_str))

    def test_get_min_cut_4(self):
        input_str = '1 2 3 4 5\n2 1 3 5\n3 1 2 4 5\n4 1 3 5\n5 1 2 3 4'
        expected_output = 3
        self.assertEqual(expected_output, KargerAlgorithm.getMinCut(input_str))

    def test_get_min_cut_5(self):
        input_str = '1 2 4 5\n2 1 5\n3 4 5\n4 1 3 5\n5 1 2 3 4'
        expected_output = 2
        self.assertEqual(expected_output, KargerAlgorithm.getMinCut(input_str))

    def test_get_min_cut_10(self):
        with open('./test_data/min_cut.txt', 'r') as file:
            input_str = file.read()

        fn_output = 17

        self.assertEqual(fn_output, KargerAlgorithm.getMinCut(input_str))
