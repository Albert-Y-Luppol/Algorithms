from src.helpers.monitoring import print_progress_bar


class KnapsackAlgorithm:
    @staticmethod
    def max_value(items: [(int, int)], capacity: int, progress_bar=False):
        last_row = [0] * (capacity + 1)
        for i in range(len(items)):
            current_row = [0] * (capacity + 1)
            v, w = items[i]
            for x in range(capacity + 1):
                current_row[x] = max(last_row[x] if i - 1 >= 0 else 0, (last_row[x-w] + v) if x - w >= 0 else 0)
            last_row = current_row
            if progress_bar:
                print_progress_bar(i, len(items), prefix='Progress:', suffix='Complete', length=50)
        return last_row[len(last_row) - 1]


    @staticmethod
    def optimal_solution(items: [(int, int)], capacity: int):
        A = [[0] * (capacity + 1) for _ in range(len(items))]
        for i in range(len(items)):
            v, w = items[i]
            for x in range(capacity + 1):
                A[i][x] = max(A[i-1][x] if i - 1 >= 0 else 0, (A[i-1][x-w] + v) if x - w >= 0 else 0)

        max_value = A[len(A) - 1][len(A[0]) - 1]
        max_weight = capacity + 1
        i = len(items) - 1
        optimal_solution = []

        while max_value > 0:
            is_i_in_optimal_solution = True if i == 0 and max_value != 0 else A[i][max_weight - 1] != A[i-1][max_weight - 1]
            if is_i_in_optimal_solution:
                v, w = items[i]
                max_weight -= w
                max_value -= v
                optimal_solution.append(items[i])
            i -= 1

        return optimal_solution

