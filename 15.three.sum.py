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

# TODO Not solve


def three_sum(nums: List[int]) -> List[List[int]]:
    target = 0
    nums.sort()
    length = len(nums)

    finish = []
    result = []

    print(nums)

    for idx in range(length):
        # if nums[idx] in finish:
        #     continue

        # finish.append(nums[idx])

        left = 1 if idx == 0 else 0
        right = length - 1 if idx != length - 1 else length - 2

        while left < right and idx not in [left, right]:
            amount = nums[idx] + nums[left] + nums[right]

            if amount == 0:
                answer = sorted([nums[left], nums[idx], nums[right]])
                if answer not in result:
                    result.append(answer)

            if amount < target:
                left += 1
            else:
                right -= 1

    print(result)
    return result


# def three_sum(nums: List[int]) -> List[List[int]]:
#     nums.sort()
#     res = []
#     for i, num in enumerate(nums):
#         box = []

#         for x in nums[i + 1 :]:
#             if x not in box:
#                 box.append(-num - x)
#             else:
#                 ans = [num, -num - x, x]

#                 if ans not in res:
#                     res.append(ans)
#     return res


if __name__ == "__main__":
    # assert three_sum([-1, 0, 1, 2, -1, -4]) == [[-1, 0, 1], [-1, -1, 2]]
    # assert three_sum([1, 2, -2, -1]) == []
    # assert three_sum([1, 2, -2]) == []
    # assert three_sum([3, 0, -2, -1, 1, 2]) == [[-2, -1, 3], [-2, 0, 2], [-1, 0, 1]]
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
