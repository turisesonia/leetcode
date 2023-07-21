"""
# 1004
Medium
Max Consecutive Ones III

https://leetcode.com/problems/max-consecutive-ones-iii

Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Example 1:
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Example 2:
Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Constraints:
1 <= nums.length <= 105
nums[i] is either 0 or 1.
0 <= k <= nums.length
"""

from typing import List


def longest_ones(nums: List[int], k: int) -> int:
    """
    leetcode 跑只贏 5% 人的解, 非常慢
    """

    max_ = 0
    # 用來當成 sliding window
    sub = []

    # zero quantity in sub
    zq = 0

    for n in nums:
        sub.append(n)

        # n = 0 時, 判斷 zq 是否比 k 大, 如果大於 k 則從 sub 左邊移除數字直到移除 0 為止
        if n == 0:
            zq += 1
            while zq > k:
                pn = sub.pop(0)
                if pn == 0:
                    zq -= 1
        max_ = max(max_, len(sub))

    return max_


def longest_ones(nums: List[int], k: int) -> int:
    """
    nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k = 2
    k 為可接受 0 的數量

    # start
    宣告兩個指標位置且都在起始位置 0
    left, right = 0, 0

    # 1
    [1]
    left = 0, right = 0, k = 2

    # 2
    [1, 1]
    left = 0, right = 1, k = 2

    # 3
    [1, 1, 1]
    left = 0, right = 2, k = 2

    # 4
    [1, 1, 1, 0]
    left = 0, right = 3, k = 1 / 0 進入 sliding window k -= 1

    # 5
    [1, 1, 1, 0, 0]
    left = 0, right = 4, k = 0 / 0 進入 sliding window k -= 1

    # 6
    [1, 1, 0, 0, 0]
    left = 1, right = 5, k = -1 / 超過可解受 0 的數量, 所以 left 也要開始移動, 讓 k 回到 0

    # 7
    [1, 0, 0, 0, 1]
    left = 2, right = 6, k = -1 / k < 0, left += 1

    # 8
    [0, 0, 0, 1, 1]
    left = 3, right = 7, k = -1 / k < 0, left += 1

    # 9
    [0, 0, 1, 1, 1]
    left = 4, right = 8, k = 0 / k 回到 0 所以 left 就可以不用移動

    # 10
    [0, 0, 1, 1, 1, 1]
    left = 4, right = 9, k = 0

    # 11
    [0, 1, 1, 1, 1, 0]
    left = 5, right = 10, k = 0

    從步驟 5 可以發現, 當 subarray 含有 k 數量的 0 時, 當下就會是目前最大的數量
    一直到步驟 10 才又多 1 進來, 所以此 nums 最長連續 1 的數量是 6
    """

    left, right = 0, 0

    while right < len(nums):
        if nums[right] == 0:
            k -= 1

        if k < 0:
            if nums[left] == 0:
                k += 1

            left += 1

        right += 1

    return right - left


if __name__ == "__main__":
    assert longest_ones([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2) == 6
    assert longest_ones([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3) == 10
