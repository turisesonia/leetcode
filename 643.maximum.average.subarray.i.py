"""
# 643
Easy
Maximum Average Subarray I

https://leetcode.com/problems/maximum-average-subarray-i

You are given an integer array nums consisting of n elements, and an integer k.
Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.
Any answer with a calculation error less than 10-5 will be accepted.

Example 1:
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Example 2:
Input: nums = [5], k = 1
Output: 5.00000

Constraints:
n == nums.length
1 <= k <= n <= 105
-104 <= nums[i] <= 104
"""
from typing import List


def find_max_average(nums: List[int], k: int) -> float:
    """
    找到長度為 k 的 subarray 其總和為最大值即是答案
    Ex:
    nums = [1, 12, -5, -6, 50, 3], k = 4

    1. 拿第一個 k=4 的 subarray 的總和當成當下的最大值
    current: sum([1, 12, -5, -6]) = 2
    max = 2

    2. 開始向右移動 (sliding window) k 長度
    [1, 12, -5, -6, 50, 3]
    [1, 12, -5, -6] -> [12, -5, -6, 50]
    對總和來說, 就是減去最左邊的元素, 加上右移後的第一個元素
    將新的 subarray 總和與先前計算的最大值比較, 取較大的存為 max 繼續往下比較

    都檢查完畢後回傳 max / k 即為答案

    O(n)
    """
    current = sum(nums[0:k])
    max_ = current

    for i in range(len(nums) - k):
        next_ = current - nums[i] + nums[i + k]
        max_ = max(max_, next_)
        current = next_

    return max_ / k


if __name__ == "__main__":
    assert find_max_average([1, 12, -5, -6, 50, 3], 4) == 12.75
    assert find_max_average([5], 1) == 5.0
    assert find_max_average([-1], 1) == -1
    assert find_max_average([0, 4, 0, 3, 2], 1) == 4
