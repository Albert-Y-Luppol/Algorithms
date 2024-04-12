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


class KnapsackHeuristicAlgorithm:
    def __init__(self, items: [(int, int)], capacity: int, error_margin=1, progress_bar=False):
        filtered_items = [item for item in items if item[1] <= capacity]
        v_max = max(items, key=lambda t: t[0])[0]
        n = len(items)
        m = int((error_margin * v_max) // n)
        optimised_items = [(value // m, space) for value, space in filtered_items]
        v_optimized_max = max(optimised_items, key=lambda t: t[0])[0]

        A = [[float('inf')] * (v_optimized_max * n + 1) for _ in range(len(items))]
        A[0][0] = 0

        progress_bar_i = 0
        progress_bar_total = n * v_optimized_max * n

        for i in range(1, len(items)):
            v_i, w_i = optimised_items[i]
            for x in range(v_optimized_max * n + 1):
                A[i][x] = min(
                    A[i-1][x],
                    (w_i if v_i >= x else w_i + A[i-1][x-v_i]))

                if progress_bar:
                    progress_bar_i += 1
                    print_progress_bar(progress_bar_i, progress_bar_total)

        max_filled_knapsack_capacity = 0
        optimised_value_for_max = None
        for x in range(v_optimized_max * n + 1):
            filled_capacity = A[n - 1][x]
            if capacity >= filled_capacity >= max_filled_knapsack_capacity:
                optimised_value_for_max = x

        # optimal solution reconstruction
        optimal_solution_indexes = []
        for i in range(n - 1, -1, -1):
            if i > 0:
                is_ith_item_included = A[i][optimised_value_for_max] != A[i-1][optimised_value_for_max]
                if is_ith_item_included:
                    optimal_solution_indexes.append(i)
                    optimised_value_for_max -= optimised_items[i][0]
            else:
                optimal_solution_indexes.append(i)

        self.knapsack_items = [filtered_items[i] for i in optimal_solution_indexes]
        self.value = sum([item[0] for item in self.knapsack_items])

