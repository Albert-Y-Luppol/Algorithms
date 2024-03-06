import unittest
from DynamicProgramming.MaximumWeightIndependentSetAlgorithm import MWIS


class MaximumWeightIndependentSetAlgorithmTest(unittest.TestCase):
    def test_1(self):
        path = [1, 1, 5, 1, 1, 5, 1, 1, 5, 1]
        mwis = MWIS(path)
        self.assertEqual([1, 1, 6, 6, 7, 11, 11, 12, 16, 16], mwis.max_weights)
        self.assertEqual('1010010010', ''.join([str(b) for b in mwis.mwis_path_bits]))

    def test_2(self):
        path = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        mwis = MWIS(path)
        self.assertEqual([1, 2, 4, 6, 9, 12, 16, 20, 25], mwis.max_weights)
        self.assertEqual('101010101', ''.join([str(b) for b in mwis.mwis_path_bits]))

    def test_3(self):
        with open('./test_data/mwis.txt', 'r') as file:
            input_str = file.read()

        path = [int(row.strip()) for row in input_str.strip().split('\n')[1:]]

        mwis = MWIS(path)
        result = [
            mwis.mwis_path_bits[0],
            mwis.mwis_path_bits[1],
            mwis.mwis_path_bits[2],
            mwis.mwis_path_bits[3],
            mwis.mwis_path_bits[16],
            mwis.mwis_path_bits[116],
            mwis.mwis_path_bits[516],
            mwis.mwis_path_bits[996],
                  ]
        self.assertEqual('10100110', ''.join([str(b) for b in result]))
