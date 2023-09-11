"""
# 303
Easy
Range Sum Query - Immutable

https://leetcode.com/problems/range-sum-query-immutable/

Given an integer array nums, handle multiple queries of the following type:

Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.

Implement the NumArray class:
NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).


Example 1:
Input
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output
[null, 1, -1, -3]

Explanation
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3

Constraints:
1 <= nums.length <= 10^4
-10^5 <= nums[i] <= 10^5
0 <= left <= right < nums.length
At most 10^4 calls will be made to sumRange.
"""

from typing import List


class NumArray:
    """
    Intuitive
    """

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left : right + 1])


class NumArray:
    def __init__(self, nums: List[int]):
        # Create previous sum array
        self.pre = [0] * (len(nums) + 1)

        """
        nums = [-2, 0, 3, -5, 2, -1]

        pre =  [0, -2, -2, 1, -4, -2, -3]

        pre[1] = sum([nums[0], nums[1]])
        pre[2] = sum([nums[0], nums[1], nums[2]])
        pre[3] = sum([nums[0], nums[1], nums[2], nums[3]])
        ...
        """

        for i in range(1, len(self.pre)):
            self.pre[i] = self.pre[i - 1] + nums[i - 1]

    def sumRange(self, left: int, right: int) -> int:
        return self.pre[right + 1] - self.pre[left]


if __name__ == "__main__":
    n1 = NumArray([-2, 0, 3, -5, 2, -1])

    assert n1.sumRange(0, 2) == 1
    assert n1.sumRange(2, 5) == -1
    assert n1.sumRange(0, 5) == -3
