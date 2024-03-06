class MWIS:
    def __init__(self, path: [int]):
        max_weights = []
        for w in path:
            max_weights.append(max(
                max_weights[-1] if len(max_weights) > 0 else 0,
                (max_weights[-2] if len(max_weights) > 1 else 0) + w,
            ))

        self.max_weights = max_weights

        mwis_path_bits = [0] * len(path)
        i = len(path) - 1
        while i >= 0:
            w = path[i]
            if (max_weights[i - 2] if i > 1 else 0) + w > (max_weights[i-1] if i > 0 else 0):
                mwis_path_bits[i] = 1
                i -= 2
            else:
                i -= 1

        self.mwis_path_bits = mwis_path_bits



