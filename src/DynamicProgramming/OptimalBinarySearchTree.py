class OptimalBinarySearchTree:
    def __init__(self, weights: [int]):
        optimal_sub_bsts_costs = [[0]*len(weights) for _ in range(len(weights))]

        longest_decimal = 0
        for w in weights:
            if '.' in str(w):
                dec_len = len(str(w).split('.')[1])
                longest_decimal = max(longest_decimal, dec_len)

        amount_of_nodes = len(weights)
        for amount_of_nodes_in_subtree in range(1, amount_of_nodes + 1):    # range() end is not inclusive
            for start_index in range(0, amount_of_nodes - amount_of_nodes_in_subtree + 1):
                end_index = start_index + amount_of_nodes_in_subtree - 1
                sum_cost = sum(weights[start_index:end_index + 1])
                min_cost = float('inf')
                for root_index in range(start_index, end_index + 1):   # when root is weights[r]
                    amount_of_nodes_in_left_bst = root_index - start_index
                    amount_of_nodes_in_right_bst = end_index - root_index
                    left_obst_cost = (0 if amount_of_nodes_in_left_bst == 0
                        else optimal_sub_bsts_costs[start_index][start_index + amount_of_nodes_in_left_bst - 1])
                    right_obst_cost = (0 if amount_of_nodes_in_right_bst == 0
                        else optimal_sub_bsts_costs[root_index + 1][root_index + amount_of_nodes_in_right_bst])
                    cost = sum_cost + left_obst_cost + right_obst_cost
                    min_cost = min(min_cost, cost)

                optimal_sub_bsts_costs[start_index][start_index + amount_of_nodes_in_subtree - 1] = round(min_cost, longest_decimal)
        self.optimal_sub_bsts_costs = optimal_sub_bsts_costs
        self.cost = optimal_sub_bsts_costs[0][amount_of_nodes - 1]


