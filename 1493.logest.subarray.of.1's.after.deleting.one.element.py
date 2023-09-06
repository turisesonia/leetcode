"""
# 1493
Medium
Longest Subarray of 1's After Deleting One Element

https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element

Given a binary array nums, you should delete one element from it.
Return the size of the longest non-empty subarray containing only 1's in the resulting array.
Return 0 if there is no such subarray.

Example 1:
Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.

Example 2:
Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].

Example 3:
Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.

Constraints:
1 <= nums.length <= 105
nums[i] is either 0 or 1.
"""


def longest_subarray(nums: list[int]) -> int:
    if 1 not in nums:
        return 0

    # there is no zero in nums, remove one element and return sum of nums
    if 0 not in nums:
        return sum(nums[1:])

    max_ = 0
    prev, sum_ = 0, 0
    i, zero_count = 0, 0

    while i < len(nums):
        if nums[i] == 0:
            zero_count += 1

            if zero_count > 1:
                # 最多只能刪除一個 0, 所以當取到第二個 0 時, 記錄前面的長度並比較是否為最大值
                max_ = max(max_, prev + sum_)
                zero_count -= 1

            prev = sum_
            sum_ = 0

        else:
            sum_ += 1

        i += 1

    max_ = max(max_, prev + sum_)

    return max_


if __name__ == "__main__":
    assert longest_subarray([1, 1, 0, 1]) == 3
    assert longest_subarray([0, 1, 1, 1, 0, 1, 1, 0, 1]) == 5
    assert longest_subarray([1, 1, 1]) == 2
    assert longest_subarray([1, 1, 0, 0]) == 2
    assert longest_subarray([1, 1, 0, 0, 1, 1, 1, 0, 1]) == 4
