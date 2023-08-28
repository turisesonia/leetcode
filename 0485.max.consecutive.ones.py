"""
# 485
Easy
Max Consecutive Ones

https://leetcode.com/problems/max-consecutive-ones/

Given a binary array nums, return the maximum number of consecutive 1's in the array.

Example 1:
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

Example 2:
Input: nums = [1,0,1,1,0,1]
Output: 2

Constraints:
1 <= nums.length <= 10^5
"""


def find_max_consecutive_ones(nums: list[int]) -> int:
    max_, sum_ = 0, 0

    for n in nums:
        if n == 0:
            max_ = max(max_, sum_)
            sum_ = 0
            continue

        sum_ += 1

    max_ = max(max_, sum_)

    return max_


if __name__ == "__main__":
    assert find_max_consecutive_ones([1, 1, 0, 1, 1, 1]) == 3
    assert find_max_consecutive_ones([1, 0, 1, 1, 0, 1]) == 2
