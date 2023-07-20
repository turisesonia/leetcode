"""
# 1679
Medium
Max Number of K-Sum Pairs

https://leetcode.com/problems/max-number-of-k-sum-pairs

You are given an integer array nums and an integer k.
In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.
Return the maximum number of operations you can perform on the array.


Example 1:
Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.

Example 2:
Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
1 <= k <= 109
"""

from typing import List


def max_operations(nums: List[int], k: int) -> int:
    """
    超過執行時間, 應該是在 nums.pop() 以及 nums.remove() 操作時花掉太多時間
    """
    ops = 0

    while len(nums) >= 2:
        target = k - nums[0]

        nums.pop(0)

        if target in nums:
            ops += 1
            nums.remove(target)

    return ops


def max_operations(nums: List[int], k: int) -> int:
    """
    使用 hash map 去記錄每個數字出現的次數,
    只計算次數大於零的情況, 找到相加等於 k 時, 就次數減一

    k - n 就是我們要找的另一個數字 (n + (k - n) == k)
    target = k - n
    """

    ops = 0
    tmp = {}

    for n in nums:
        target = k - n

        if tmp.get(target, 0) > 0:
            ops += 1
            tmp[target] -= 1
        else:
            tmp[n] = tmp.get(n, 0) + 1

    return ops


if __name__ == "__main__":
    assert max_operations([1, 2, 3, 4], 5) == 2
    assert max_operations([3, 1, 3, 4, 3], 6) == 1
    assert max_operations([2, 5, 4, 4, 1, 3, 4, 4, 1, 4, 4, 1, 2, 1, 2, 2, 3, 2, 4, 2], 3) == 4
