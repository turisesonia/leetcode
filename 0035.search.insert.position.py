"""
# 35
Easy

https://leetcode.com/problems/search-insert-position/

Search insert position

Given a sorted array of distinct integers and a target value,
return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4
"""
from typing import List


def search_insert(nums: List[int], target: int) -> int:
    """
    此解法並不符合題目的 O(log n) 時間複雜度
    """
    length = len(nums)

    for i in range(length):
        # 數值相同或者超過時就 return position
        if nums[i] == target or nums[i] > target:
            return i

    return length


def search_insert(nums: List[int], target: int) -> int:
    """
    題目要求要符合時間複雜度 O(log n), 所以此題要用二元搜尋法 (Binary search) 來找出要插入的位置
    給定的 nums 為小至大排序且不會有重複的數字

    取得 l, r 為 nums 的頭尾 index, 每次用這段區間的中間值 (mid) 與 target 比較大小

    1. target == mid 就返回 mid 的位置
    2. target > mid 只需要再找 mid + 1 ~ r 這段區間
    3. target < mid 只需要再找 l ~ mid - 1 這段區間
    4. 最後返回 l 就是要插入的位置
    """
    l, r = 0, len(nums) - 1
    mi = (l + r) // 2

    while l <= r:
        if target == nums[mi]:
            return mi

        if target > nums[mi]:
            l = mi + 1
        else:
            r = mi - 1

        mi = (l + r) // 2

    return l


if __name__ == "__main__":
    assert search_insert([1, 3, 5, 6], 5) == 2
    assert search_insert([1, 3, 5, 6], 2) == 1
    assert search_insert([1, 3, 5, 6], 7) == 4
    assert search_insert([1, 3, 5, 6], 0) == 0
