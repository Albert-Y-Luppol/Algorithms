import re
import unittest
from src.Graphs.TwoSatProblem import PapadimitriousAlgorithm, StronglyConnectedComponents


class TwoSatProblemTest(unittest.TestCase):
    def test_0_papadimitrious_algorithm(self):
        n_of_vars = 3
        clauses = [(1, -2), (-2, 3), (1, 3)]

        self.assertTrue(PapadimitriousAlgorithm.is_assignment_available(n_of_vars, clauses))

    def test_1_papadimitrious_algorithm(self):
        n_of_vars = 3
        clauses = [(1, -2), (2, 3), (-1, -3)]

        self.assertTrue(PapadimitriousAlgorithm.is_assignment_available(n_of_vars, clauses))

    def test_2_papadimitrious_algorithm(self):
        n_of_vars = 2
        clauses = [(1, -2), (1, 2), (-1, -2), (-1, 2)]

        self.assertFalse(PapadimitriousAlgorithm.is_assignment_available(n_of_vars, clauses, loader=True))

    def test_3_papadimitrious_algorithm(self):
        with open('test_data/2sat1.txt') as file:
            input_str = file.read()

        rows = input_str.strip().split('\n')
        bool_n = int(rows[0])
        clauses_str = [tuple(re.split(r'\s+', row.strip())) for row in rows[1:]]
        clauses = [(int(x_i), int(x_j)) for x_i, x_j in clauses_str]

        self.assertEqual(True, PapadimitriousAlgorithm.is_assignment_available(bool_n, clauses, loader=True))

    def test_4_scc_algorithm(self):
        clauses = [(1, -2), (-2, 3), (1, 3)]
        self.assertTrue(StronglyConnectedComponents.is_assignment_available(clauses))

    def test_5_scc_algorithm(self):
        clauses = [(1, -2), (1, 2), (-1, -2), (-1, 2)]
        self.assertFalse(StronglyConnectedComponents.is_assignment_available(clauses))

    def test_6_scc_algorithm(self):
        with open('test_data/2sat1.txt') as file:
            input_str = file.read()

        rows = input_str.strip().split('\n')
        clauses_str = [tuple(re.split(r'\s+', row.strip())) for row in rows[1:]]
        clauses = [(int(x_i), int(x_j)) for x_i, x_j in clauses_str]

        self.assertEqual(True, StronglyConnectedComponents.is_assignment_available(clauses, loader=True))

    def test_7_scc_algorithm(self):
        with open('test_data/2sat2.txt') as file:
            input_str = file.read()

        rows = input_str.strip().split('\n')
        clauses_str = [tuple(re.split(r'\s+', row.strip())) for row in rows[1:]]
        clauses = [(int(x_i), int(x_j)) for x_i, x_j in clauses_str]

        self.assertEqual(False, StronglyConnectedComponents.is_assignment_available(clauses, loader=True))

    def test_8_scc_algorithm(self):
        with open('test_data/2sat3.txt') as file:
            input_str = file.read()

        rows = input_str.strip().split('\n')
        clauses_str = [tuple(re.split(r'\s+', row.strip())) for row in rows[1:]]
        clauses = [(int(x_i), int(x_j)) for x_i, x_j in clauses_str]

        self.assertEqual(True, StronglyConnectedComponents.is_assignment_available(clauses, loader=True))

    def test_9_scc_algorithm(self):
        with open('test_data/2sat4.txt') as file:
            input_str = file.read()

        rows = input_str.strip().split('\n')
        clauses_str = [tuple(re.split(r'\s+', row.strip())) for row in rows[1:]]
        clauses = [(int(x_i), int(x_j)) for x_i, x_j in clauses_str]

        self.assertEqual(True, StronglyConnectedComponents.is_assignment_available(clauses, loader=True))

    def test_10_scc_algorithm(self):
        with open('test_data/2sat5.txt') as file:
            input_str = file.read()

        rows = input_str.strip().split('\n')
        clauses_str = [tuple(re.split(r'\s+', row.strip())) for row in rows[1:]]
        clauses = [(int(x_i), int(x_j)) for x_i, x_j in clauses_str]

        self.assertEqual(False, StronglyConnectedComponents.is_assignment_available(clauses, loader=True))

    def test_11_scc_algorithm(self):
        with open('test_data/2sat6.txt') as file:
            input_str = file.read()

        rows = input_str.strip().split('\n')
        clauses_str = [tuple(re.split(r'\s+', row.strip())) for row in rows[1:]]
        clauses = [(int(x_i), int(x_j)) for x_i, x_j in clauses_str]

        self.assertEqual(False, StronglyConnectedComponents.is_assignment_available(clauses, loader=True))
