"""
# 27
Remove Element
Easy

https://leetcode.com/problems/remove-element/?envType=study-plan-v2&envId=top-interview-150

Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:
Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.

Example 1:
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:
Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).

Constraints:

0 <= nums.length <= 100
0 <= nums[i] <= 50
0 <= val <= 100
"""
from typing import List


def remove_element(nums: List[int], val: int) -> int:
    """
    利用 list pop 來處理 element == val 的情況
    因為 pop 後整個 list 長度會縮小 1, 所以在 pop element 時需要將 total - 1
    """
    i = 0
    total = len(nums)

    while i < total:
        if nums[i] == val:
            nums.pop(nums[i])
            total -= 1
        else:
            i += 1

    return total


def remove_element(nums: List[int], val: int) -> int:
    """
    python 專用解法
    """
    for n in nums:
        if n == val:
            nums.remove(n)

    return len(nums)


if __name__ == "__main__":
    assert remove_element([3, 2, 2, 3], 3) == 2
