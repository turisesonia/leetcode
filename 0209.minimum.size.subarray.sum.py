"""
# 209
Medium
Minimum Size Subarray Sum

https://leetcode.com/problems/minimum-size-subarray-sum

Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target.
If there is no such subarray, return 0 instead.

Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0

Constraints:
* 1 <= target <= 10^9
* 1 <= nums.length <= 10^5
* 1 <= nums[i] <= 10^4

Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).
"""

from typing import List


def min_sub_array_len(target: int, nums: List[int]) -> int:
    # no such subarray when sum of nums small than target
    if sum(nums) < target:
        return 0

    min_len = len(nums)
    # left, right pointer for sliding window
    left, right = 0, 0
    sum_ = nums[0]

    while left <= right and right < len(nums):
        if sum_ < target:
            right += 1

            # prevent right out of index
            if right < len(nums):
                sum_ += nums[right]

        else:
            min_len = min(min_len, right - left + 1)

            sum_ -= nums[left]
            left += 1

    return min_len


if __name__ == "__main__":
    assert min_sub_array_len(target=7, nums=[2, 3, 1, 2, 4, 3]) == 2
    assert min_sub_array_len(target=4, nums=[1, 4, 4]) == 1
    assert min_sub_array_len(target=11, nums=[1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert min_sub_array_len(target=11, nums=[1, 2, 3, 4, 5]) == 3
