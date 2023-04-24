import numpy as np
from scipy.optimize import linear_sum_assignment

class HungarianAlgorithm:
    @staticmethod
    def optimal_assignment(matrix: [[str]]) -> str:
        cost_matrix = np.array([list(map(int, row.split())) for row in matrix])
        row_ind, col_ind = linear_sum_assignment(cost_matrix)
        print(row_ind, col_ind)

        result = ''
        for task, computer in zip(row_ind, col_ind):
            result += f'({task+1}-{computer+1})'

        return result
