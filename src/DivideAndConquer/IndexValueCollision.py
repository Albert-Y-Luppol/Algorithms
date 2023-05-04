# You are given a sorted (from smallest to largest) array A of n distinct integers which can be positive, negative,
# or zero. You want to decide whether or not there is an index i such that A[i] = i. Design the fastest algorithm that
# you can for solving this problem.
def indexValueCollision(l: [int], start=0, end=None) -> bool: # O(log(n))
    if end is None:
        end = len(l) - 1

    if start > end:
        return False

    i = (end + start) // 2

    if l[i] == i:
        return True

    if i > l[i]:
        return indexValueCollision(l, i + 1, end)
    else:
        return indexValueCollision(l, start, i - 1)

