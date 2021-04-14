"""
Given a list of integers numbers "nums".
You need to find a sub-array with length less equal to "k", with maximal sum.
The written function should return the sum of this sub-array.
Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    """Find a sub-array with length less equal to "k", with maximal sum in list of integers"""

    nums_begin = nums[:k]
    max_sum = sum(nums_begin)
    for num in nums[k:]:
        nums_begin = nums_begin[1:]
        nums_begin.append(num)
        if sum(nums_begin) > max_sum:
            max_sum = sum(nums_begin)
    return max_sum
