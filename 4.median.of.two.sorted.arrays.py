"""
#4
Median of Two Sorted Arrays
Hard

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
"""
import math
from typing import List


def find_median_sorted_arrays(nums1: List[int], nums2: List[int]) -> float:
    """
    用了 python 提供的 sorted 來解, 待研究不使用 sorted 的解法
    """
    merged = sorted(nums1 + nums2)
    length = len(merged)

    if length % 2:
        res = merged[math.floor(length / 2)]

    else:
        half = int(length / 2)
        res = (merged[half - 1] + merged[half]) / 2

    return res


if __name__ == "__main__":
    assert find_median_sorted_arrays([1, 3], [2]) == 2.0
    assert find_median_sorted_arrays([1, 3], [2, 3]) == 2.5
    assert find_median_sorted_arrays([1, 2], [3, 4]) == 2.5
