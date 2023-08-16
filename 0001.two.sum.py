"""
# 1
Easy
https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""


def two_sum(nums: list, target: int):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    elements = {}

    for i in range(len(nums)):
        # 利用 target 減去現在的位置數字並在暫存的 dict 裡找 index
        if target - nums[i] in elements:
            return [elements[target - nums[i]], i]

        # 將現在的數字索引存在 elements 內
        elements[nums[i]] = i


def two_sum(nums: list, target: int):
    tmp = {}

    for idx, num in enumerate(nums):
        ans = target - num

        if ans in tmp:
            return [tmp[ans], idx]

        tmp[num] = idx


if __name__ == "__main__":
    assert two_sum(nums=[2, 7, 11, 15], target=9) == [0, 1]
    assert two_sum(nums=[1, 6, 3, 4, 8], target=14) == [1, 4]
    assert two_sum(nums=[3, 2, 4], target=6) == [1, 2]
    assert two_sum(nums=[3, 3], target=6) == [0, 1]
