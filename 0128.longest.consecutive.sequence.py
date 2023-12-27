"""
# 128
Medium
Longest Consecutive Sequence

https://leetcode.com/problems/longest-consecutive-sequence

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

! You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Constraints:
* 0 <= nums.length <= 10^5
* -10^9 <= nums[i] <= 10^9
"""


def longest_consecutive(nums: list[int]) -> int:
    """
    ! Not O(n) solution
    """
    nums_len = len(nums)
    if nums_len <= 1:
        return nums_len

    nums.sort()
    s = set()
    longest = 0
    consecutive = 1
    prefix = nums[0]

    for num in nums:
        if num in s:
            continue

        if num - 1 == prefix:
            consecutive += 1
        else:
            consecutive = 1

        prefix = num
        s.add(num)
        longest = max(longest, consecutive)

    return longest


def longest_consecutive(nums: list[int]) -> int:
    """
    ! O(n)
    """
    set_ = set(nums)
    longest = 0

    for num in nums:
        before = num - 1

        if before not in set_:
            k = num
            cons = 0
            while k in set_:
                cons += 1
                k += 1

            longest = max(longest, cons)

    return longest


if __name__ == "__main__":
    assert longest_consecutive(nums=[100, 4, 200, 1, 3, 2]) == 4
    assert longest_consecutive(nums=[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
    assert longest_consecutive(nums=[1, 2, 0, 1]) == 3
    assert longest_consecutive(nums=[0]) == 1
    assert longest_consecutive(nums=[0, 0]) == 1
    assert longest_consecutive(nums=[]) == 0
