"""
# 219
Easy
Contains Duplicate II

https://leetcode.com/problems/contains-duplicate-ii/

Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.


Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105
"""


def contains_nearby_duplicate(nums: list[int], k: int) -> bool:
    """
    用 sliding window 的方式解, 速度太慢不適合
    """
    tmp = []

    for n in nums:
        if len(tmp) > k:
            tmp.pop(0)

        if n in tmp:
            return True
        else:
            tmp.append(n)

    return False


def contains_nearby_duplicate(nums: list[int], k: int) -> bool:
    """
    用 dict 儲存已出現過數字的 index, 當再次出現同樣數字時
    計算上一個出現的 index (i) 與當下所在的 index (j) 的絕對值差是否小於等於 k -> abs(i - j) <= k
    """

    hm = {}

    for i in range(len(nums)):
        n = nums[i]

        if n in hm and abs(i - hm[n]) <= k:
            return True
        else:
            hm[n] = i

    return False


if __name__ == "__main__":
    assert contains_nearby_duplicate([1, 2, 3, 1], 3)
    assert contains_nearby_duplicate([1, 0, 1, 1], 1)
    assert not contains_nearby_duplicate([1, 2, 3, 1, 2, 3], 2)
    assert contains_nearby_duplicate([1, 2, 3, 4, 5, 6, 7, 8, 9, 9], 3)
