"""
# 136
Easy
Single Number

https://leetcode.com/problems/single-number/

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1

Constraints:
1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.
"""

from typing import List


def single_number(nums: List[int]) -> int:
    """
    將 nums 排序後, 找到前後都不一樣時, 就是唯一沒出現兩次的數字

    Ex: [4, 1, 2, 1, 2] -> (sorted) [1, 1, 2, 2, 4]
    """

    if len(nums) == 1:
        return nums[0]

    nums.sort()

    for i in range(len(nums)):
        if i >= 0 and nums[i - 1] == nums[i]:
            continue

        if i < len(nums) - 1 and nums[i] == nums[i + 1]:
            continue

        return nums[i]


def single_number(nums: List[int]) -> int:
    """
    運用 python XOR 的特性

    0 ^ 0 = 0
    0 ^ 1 = 1
    1 ^ 0 = 1
    1 ^ 1 = 0
    """

    res = 0
    for n in nums:
        res ^= n

    return res


if __name__ == "__main__":
    assert single_number([2, 2, 1]) == 1
    assert single_number([4, 1, 2, 1, 2]) == 4
    assert single_number([1]) == 1
