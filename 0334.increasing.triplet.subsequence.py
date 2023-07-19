"""
# 334
Medium
Increasing Triplet Subsequence

https://leetcode.com/problems/increasing-triplet-subsequence

Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k].
If no such indices exists, return false.

Example 1:
Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.

Example 2:
Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.

Example 3:
Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.

Constraints:
1 <= nums.length <= 5 * 105
-231 <= nums[i] <= 231 - 1

Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?
"""
from typing import List


def increasing_triplet(nums: List[int]) -> bool:
    i = 1
    length = len(nums)
    min_, max_ = min(nums), max(nums)

    while i < length - 1:
        if min_ != nums[i] and nums[i] != max_:
            return True

        i += 1

    return False


def increasing_triplet(nums: List[int]) -> bool:
    f = float("inf")
    s = float("inf")

    for n in nums:
        # If n is less than f, it means n can be a potential candidate for the first element of an increasing triplet subsequence. So, it updates f to n.
        if n <= f:
            f = n
        # If n is greater than f and less than s, it means n can be a potential candidate for the second element of an increasing triplet subsequence. So, it updates s to n.
        elif n <= s:
            s = n
        # If n is greater than both f and s, it indicates the presence of an increasing triplet subsequence. So, it returns True.
        else:
            print("------", f, s, n)
            return True

        print(f, s, n)

    # If the loop completes without finding an increasing triplet subsequence, it means there is no such subsequence in the array, so it returns False.
    return False


if __name__ == "__main__":
    # assert increasing_triplet([1, 2, 3, 4, 5])
    # assert not increasing_triplet([5, 4, 3, 2, 1])
    # assert increasing_triplet([2, 1, 5, 0, 4, 6])
    assert increasing_triplet([20, 100, 10, 12, 5, 13])
