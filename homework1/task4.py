"""
Classic task, a kind of walnut for you
Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.
We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from typing import List


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    tup_count = 0
    for a_elem in a:
        for b_elem in b:
            for c_elem in c:
                for d_elem in d:
                    if a_elem + b_elem + c_elem + d_elem == 0:
                        tup_count += 1
    return tup_count
