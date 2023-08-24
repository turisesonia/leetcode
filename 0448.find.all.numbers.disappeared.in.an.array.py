"""
# 448
Easy
Find All Numbers Disappeared in an Array

https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

Example 1:
Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]

Example 2:
Input: nums = [1,1]
Output: [2]

Constraints:
n == nums.length
1 <= n <= 105
1 <= nums[i] <= n

Follow up:
Could you do it without extra space and in O(n) runtime?
You may assume the returned list does not count as extra space.
"""


def find_disappeared_numbers(nums: list[int]) -> list[int]:
    """
    Solved using XOR two sets

    (Use a lot of memory if n is large)
    """
    n = len(nums)

    full = {n for n in range(1, n + 1)}

    return list(full ^ set(nums))


def find_disappeared_numbers(nums: list[int]) -> list[int]:
    n = len(nums)

    nums = set(nums)

    res = []
    for i in range(1, n + 1):
        if i not in nums:
            res.append(i)

    return res


def find_disappeared_numbers(nums: list[int]) -> list[int]:
    """
    1. Iterate through the input list nums, and for each element nums[i]:
        a. Calculate the index of nums[i] in the list by taking the absolute value of nums[i] and subtracting 1. This is because the input list contains integers in the range [1, n].
        b. Update the value at the calculated index to its negative absolute value using nums[index] = -abs(nums[index]). This is because the input list can contain duplicates, so we need to mark the value as visited using its absolute value.
    2. Iterate through the updated list nums, and for each element nums[i]:
        a. If the value at index i is positive, it means that the number i+1 did not appear in the input list. Append i+1 to the list of missing numbers.
    3. Return the list of missing numbers.
    """
    for i in range(len(nums)):
        index = abs(nums[i]) - 1
        nums[index] = -abs(nums[index])

    # collect the missing values which are still positive
    missing = []
    for i in range(len(nums)):
        if nums[i] > 0:
            missing.append(i + 1)

    return missing


if __name__ == "__main__":
    assert find_disappeared_numbers([4, 3, 2, 7, 8, 2, 3, 1]) == [5, 6]
    assert find_disappeared_numbers([1, 1]) == [2]
