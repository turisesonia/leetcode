"""
# 15
3 Sum
Medium

https://leetcode.com/problems/3sum/

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.


Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105

"""

from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    # sort the nums list in ascending order
    nums.sort()
    length = len(nums)
    visited = set()

    result = []
    for i in range(length):
        num = nums[i]

        # Since the nums list is already sorted in ascending order,
        # there are no pairs of numbers that can sum to zero if nums[i] is greater than zero.
        if num in visited or num > 0:
            continue

        visited.add(num)

        # fixed current position x
        target = -1 * num

        # two pointer to find y, z which y + z = -x
        left, right = i + 1, length - 1

        while left < right:
            sum_ = nums[left] + nums[right]
            if sum_ < target:
                left += 1
            elif sum_ > target:
                right -= 1
            else:
                result.append([num, nums[left], nums[right]])
                left += 1
                # handle same number
                while nums[left] == nums[left - 1] and left < right:
                    left += 1

    return result


if __name__ == "__main__":
    assert three_sum([-2, 0, 1, 1, 2]) == [[-2, 0, 2], [-2, 1, 1]]
    assert three_sum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert three_sum([1, 2, -2, -1]) == []
    assert three_sum([1, 2, -2]) == []
    assert three_sum([3, 0, -2, -1, 1, 2]) == [[-2, -1, 3], [-2, 0, 2], [-1, 0, 1]]
    assert three_sum([0, 0, 0]) == [[0, 0, 0]]
    assert three_sum([-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]) == [
        [-4, 0, 4],
        [-4, 1, 3],
        [-3, -1, 4],
        [-3, 0, 3],
        [-3, 1, 2],
        [-2, -1, 3],
        [-2, 0, 2],
        [-1, -1, 2],
        [-1, 0, 1],
    ]
