"""
# 169
Easy
Majority Element

https://leetcode.com/problems/majority-element/

Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109

Follow-up: Could you solve the problem in linear time and in O(1) space?
"""

from typing import List


def majority_element(nums: List[int]) -> int:
    hm = {}

    for n in nums:
        if n not in hm:
            hm[n] = 1

        else:
            hm[n] += 1

        if hm[n] > len(nums) / 2:
            return n


def majority_element(nums: List[int]) -> int:
    nums.sort()

    return nums[len(nums) // 2]


if __name__ == "__main__":
    assert majority_element([3, 2, 3]) == 3
    assert majority_element([2, 2, 1, 1, 1, 2, 2]) == 2
