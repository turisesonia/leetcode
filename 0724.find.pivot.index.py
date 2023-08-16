"""
# 724
Easy
Find Pivot Index

https://leetcode.com/problems/find-pivot-index

Given an array of integers nums, calculate the pivot index of this array.
The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.
If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left.
This also applies to the right edge of the array.
Return the leftmost pivot index. If no such index exists, return -1.

Example 1:
Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11

Example 2:
Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.

Example 3:
Input: nums = [2,1,-1]
Output: 0
Explanation:
The pivot index is 0.
Left sum = 0 (no elements to the left of index 0)
Right sum = nums[1] + nums[2] = 1 + -1 = 0

Constraints:
1 <= nums.length <= 104
-1000 <= nums[i] <= 1000
"""

from typing import List


def pivot_index(nums: List[int]) -> int:
    """
    第一次直覺解
    檢查到每個位置時都取出左 / 右的 subarray 並加總比較
    因為每次都要切割兩邊的 subarray, 造成執行時間非常長
    """
    i = 0

    while i < len(nums):
        left = sum(nums[:i])
        right = sum(nums[i + 1 :])

        if left == right:
            return i

        i += 1

    return -1


def pivot_index(nums: List[int]) -> int:
    """
    重新思考題目後的解
    因為是要找出 pivot index 左右的元素"加總"相等時

    [1, 7, 3, 6, 5, 6]
    宣告 3 個變數
    i = 0             # 判斷到第幾個位置
    prev = 0          # 記錄前一次左邊加總的和
    total = sum(nums) # total array sum, # 28

    由左至右檢查 nums 中的位置, 如果找到左右和相等的時候就回傳 i

    # step 1
    i = 0
    prev = 0
    ["1", 7, 3, 6, 5, 6]
    left == prev (因為在最左邊, 所以左和 = 0)
    right == (7+3+6+5+6) == total - nums[i] - prev == 28 - 1 - 0

    left 不等於 right, i 不是我們要找的 pivot index,
    i += 1
    prev += nums[i]

    # step 2
    i = 1
    prev = 1
    [1, "7", 3, 6, 5, 6]
    上一步最後都會計算 prev 的值 prev 就會剛好為左邊加總
    所以計算 right 即可
    right = total - nums[i] - prev

    持續檢查到 left == right 或者到最後回傳 -1
    """
    i, prev, total = 0, 0, sum(nums)

    while i < len(nums):
        left = prev
        right = total - nums[i] - prev

        if left == right:
            return i

        prev = prev + nums[i]

        i += 1

    return -1


if __name__ == "__main__":
    assert pivot_index([1, 7, 3, 6, 5, 6]) == 3
    assert pivot_index([1, 2, 3]) == -1
    assert pivot_index([2, 1, -1]) == 0
