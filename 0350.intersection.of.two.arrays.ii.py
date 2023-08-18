"""
# 350
Easy
Intersection of Two Arrays II

https://leetcode.com/problems/intersection-of-two-arrays-ii/

Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.

Constraints:
1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000

Follow up:
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
"""


def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
    """
    Solutions using list and remove
    """
    res = []

    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    for n in nums1:
        if n in nums2:
            res.append(n)
            nums2.remove(n)

    return res


def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
    """
    Solution using hash map
    """
    hm = {}
    res = []

    for n in nums1:
        hm[n] = hm.get(n, 0) + 1

    for n in nums2:
        if n in hm and hm[n] > 0:
            res.append(n)
            hm[n] -= 1

    return res


if __name__ == "__main__":
    assert intersection([1, 2, 2, 1], [2, 2]) == [2, 2]
    assert intersection([4, 9, 5], [9, 4, 9, 8, 4]) in ([9, 4], [4, 9])
