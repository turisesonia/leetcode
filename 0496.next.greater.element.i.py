"""
# 496
Easy
Next Greater Element I

https://leetcode.com/problems/next-greater-element-i/

The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.
You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.
For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2.
If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

Example 1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.

Example 2:
Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
- 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.

Constraints:
1 <= nums1.length <= nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 104
All integers in nums1 and nums2 are unique.
All the integers of nums1 also appear in nums2.

Follow up: Could you find an O(nums1.length + nums2.length) solution?
"""


def next_greater_element(nums1: list[int], nums2: list[int]) -> list[int]:
    """
    O(n1 * n2)
    """
    nums2_len = len(nums2)

    ans = []
    for num in nums1:
        i = nums2.index(num)

        if i == nums2_len - 1:
            ans.append(-1)
            continue

        for j in range(i + 1, nums2_len):
            n = nums2[j]
            if n >= num:
                ans.append(n)
                break
        else:
            ans.append(-1)

    return ans


def next_greater_element(nums1: list[int], nums2: list[int]) -> list[int]:
    # O(n1 + n2)

    ans = []
    stack = []
    hm = {}

    # use stack find every element next greater element in nums2
    for i in range(len(nums2)):
        n = nums2[i]
        while stack and n > stack[-1]:
            hm[stack.pop()] = n

        stack.append(n)

    for num in nums1:
        ans.append(hm.get(num, -1))

    return ans


if __name__ == "__main__":
    assert next_greater_element([4, 1, 2], [1, 3, 4, 2]) == [-1, 3, -1]
    assert next_greater_element([2, 4], [1, 2, 3, 4]) == [3, -1]
    assert next_greater_element([1, 3, 5, 2, 4], [6, 5, 4, 3, 2, 1, 7]) == [7, 7, 7, 7, 7]
