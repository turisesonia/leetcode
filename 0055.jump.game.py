"""
# 55
Medium
Jump Game

https://leetcode.com/problems/jump-game

You are given an integer array nums.
You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.

Example 1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

Constraints:
* 1 <= nums.length <= 10^4
* 0 <= nums[i] <= 10^5
"""


def can_jump(nums: list[int]) -> bool:
    """
    Check every item from the last second to the first
    ex: [2,3,1,1,4] -> [4, 1, 1, 3, 2];

    The needed variable represents the number of steps jump to the last position from current position
    We start at the last second item, and set `needed` value is "1", because there just need one step to get the end.
    """

    if len(nums) <= 1:
        return True

    needed = 1
    for i in range(len(nums) - 2, -1, -1):
        n = nums[i]

        if n >= needed:
            # 可走的步數 >= 所需的步數，代表此位置可以走到最後一個位置
            nums[i] = True
            # 重設所需的步數，下一次迴圈只需判斷是否可以走到這個位置
            needed = 1
        else:
            # 因為此位置無法走到最後，在下一次迴圈時所需的步數會加 1
            nums[i] = False
            needed += 1

    return nums[0]


if __name__ == "__main__":
    assert can_jump(nums=[2, 3, 1, 1, 4])
    assert not can_jump(nums=[3, 2, 1, 0, 4])
    assert can_jump(nums=[0])
    assert not can_jump(nums=[0, 1])
    assert can_jump(nums=[2, 0, 0])
    assert can_jump(nums=[1, 2, 0, 1])
