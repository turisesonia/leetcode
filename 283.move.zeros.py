"""
# 283
Easy
Move Zeroes

https://leetcode.com/problems/move-zeroes/?envType=study-plan-v2&envId=leetcode-75

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]

Constraints:
1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
"""

from typing import List


def move_zeroes(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    i, j = 0, 1

    while j < len(nums):
        if nums[i] != 0:
            i += 1
            j += 1
            continue

        if nums[j] == 0:
            j += 1
            continue

        if nums[i] == 0 and nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]


if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]
    move_zeroes(nums)
    assert nums == [1, 3, 12, 0, 0]

    nums = [0]
    move_zeroes(nums)
    assert nums == [0]

    nums = [2, 1]
    move_zeroes(nums)
    assert nums == [2, 1]

    nums = [4, 2, 4, 0, 0, 3, 0, 5, 1, 0]
    move_zeroes(nums)
    assert nums == [4, 2, 4, 3, 5, 1, 0, 0, 0, 0]
