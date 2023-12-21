"""
# 88
Easy
Merge Sorted Array

https://leetcode.com/problems/merge-sorted-array/

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Example 1:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

Example 2:
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].

Example 3:
Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.

Constraints:
* nums1.length == m + n
* nums2.length == n
* 0 <= m, n <= 200
* 1 <= m + n <= 200
* -10^9 <= nums1[i], nums2[j] <= 10^9
"""

from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.

    nums1 = [4, 5, 6, 0, 0, 0], nums2 = [1, 2, 3]
    n1i = 2, n2i = 2, ins = 5

    # 1
    - 6 > 3
    nums1 = [4, 5, 6, 0, 0, 6], n1i = 1, n2i = 2, ins = 4

    # 2
    - 5 > 3
    nums1 = [4, 5, 6, 0, 5, 6], n1i = 0, n2i = 2, ins = 3

    # 3
    - 4 > 3
    nums1 = [4, 5, 6, 4, 5, 6], n1i = -1, n2i = 2, ins = 2

    # 4
    - n1i < 0
    nums1 = [4, 5, 3, 4, 5, 6], n1i = -1, n2i = 1, ins = 1

    # 5
    - n1i < 0
    nums1 = [4, 2, 3, 4, 5, 6], n1i = -1, n2i = 0, ins = 0

    # 6
    - n1i < 0
    nums1 = [1, 2, 3, 4, 5, 6], n1i = -1, n2i = -1, ins = -1
    """
    # nums1 and nums2 current position, from last to start
    n1i = m - 1
    n2i = n - 1

    # number insert current postion
    ins = m + n - 1

    while n2i >= 0:
        if n1i >= 0 and nums1[n1i] > nums2[n2i]:
            # n1i 存在且數字大於 n2i 時, 將此數字放置最後面
            nums1[ins] = nums1[n1i]
            n1i -= 1
        else:
            # n2i 直接放在 ins 的位置
            nums1[ins] = nums2[n2i]
            n2i -= 1

        ins -= 1


if __name__ == "__main__":
    # * Case 1
    nums1 = [1, 2, 3, 0, 0, 0]
    merge(nums1, 3, [2, 5, 6], 3)

    print(nums1)
    assert nums1 == [1, 2, 2, 3, 5, 6]

    # * Case 2
    nums1 = [1]
    merge(nums1, 1, [], 0)

    print(nums1)
    assert nums1 == [1]

    # * Case 3
    nums1 = [0]
    merge(nums1, 0, [1], 1)

    print(nums1)
    assert nums1 == [1]

    # * Case 4
    nums1 = [2, 0]
    merge(nums1, 1, [1], 1)

    print(nums1)
    assert nums1 == [1, 2]

    # * Case 5
    nums1 = [0, 0, 0, 0, 0]
    merge(nums1, 0, [1, 2, 3, 4, 5], 5)

    print(nums1)
    assert nums1 == [1, 2, 3, 4, 5]

    # * Case 6
    nums1 = [4, 5, 6, 0, 0, 0]
    merge(nums1, 3, [1, 2, 3], 3)

    print(nums1)
    assert nums1 == [1, 2, 3, 4, 5, 6]

    # * Case 7
    nums1 = [4, 0, 0, 0, 0, 0]
    merge(nums1, 1, [1, 2, 3, 5, 6], 5)

    print(nums1)
    assert nums1 == [1, 2, 3, 4, 5, 6]
