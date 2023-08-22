"""
# 414
Easy
Third Maximum Number

https://leetcode.com/problems/third-maximum-number/

Given an integer array nums, return the third distinct maximum number in this array.
If the third maximum does not exist, return the maximum number.

Example 1:
Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.

Example 2:
Input: nums = [1,2]
Output: 2
Explanation:
The first distinct maximum is 2.
The second distinct maximum is 1.
The third distinct maximum does not exist, so the maximum (2) is returned instead.

Example 3:
Input: nums = [2,2,3,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2 (both 2's are counted together since they have the same value).
The third distinct maximum is 1.

Constraints:
1 <= nums.length <= 104
-2^31 <= nums[i] <= 2^31 - 1

Follow up: Can you find an O(n) solution?
"""


def third_max(nums: list[int]) -> int:
    nums = sorted(set(nums))

    if len(nums) >= 3:
        return nums[-3]
    else:
        return nums[-1]


def third_max(nums: list[int]) -> int:
    # float("inf") represents a number bigger than any other numbers
    # float("-inf") represents a number smaller than any other numbers
    first = second = third = float("-inf")

    # get unique numbers in nums
    uniq = set(nums)

    for n in uniq:
        if n > first:
            third = second
            second = first
            first = n

        elif n > second:
            third = second
            second = n

        elif n > third:
            third = n

    return third if len(uniq) >= 3 else first


if __name__ == "__main__":
    assert third_max([3, 2, 1]) == 1
    assert third_max([1, 2]) == 2
    assert third_max([2, 2, 3, 1]) == 1
