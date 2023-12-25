"""
# 45
Medium
Jump Game II

https://leetcode.com/problems/jump-game-ii

You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
Each element nums[i] represents the maximum length of a forward jump from index i.

In other words, if you are at nums[i], you can jump to any nums[i + j] where:
    - 0 <= j <= nums[i] and
    - i + j < n

Return the minimum number of jumps to reach nums[n - 1].
The test cases are generated such that you can reach nums[n - 1].



Example 1:
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [2,3,0,1,4]
Output: 2

Constraints:
* 1 <= nums.length <= 10^4
* 0 <= nums[i] <= 1000
* It's guaranteed that you can reach nums[n - 1].
"""


def jump(nums: list[int]) -> int:
    """
    在每次可以走到的所有位置中, 盡量選擇最大的
    Ex: [2, 3, 1, 1, 4]

    1. index = 0, value = 2
    可以走 1 ~ 2 步, 抵達的位置值為 (3, 1) 依照一開始的策略選擇走到 3 這個位置

    2. index = 1, value = 3
    可以走 1 ~ 3 步, 走 3 步即抵達終點

    Ex: [1, 2, 1, 1, 1]

    1. index = 0, value = 1
    可以走 1 步, 抵達的位置 2

    2. index = 1, value = 2
    可以走 1 ~ 2 步, 抵達位置為 list[(value, index)] = [(1, 2), (1, 3)]
    在這種情況, 因為可選的選擇中, 值都是一樣大的, 要盡可能往右邊選
    所以這裡的判斷是選 (1, 3)
    """

    length = len(nums)
    i = 0
    jumped = 0

    while i < length - 1:
        options = []
        for j in range(1, nums[i] + 1):
            pos = i + j
            if pos >= length:
                break

            val = float("inf") if pos == length - 1 else nums[pos] + pos
            options.append((val, pos))

        option = max(options, key=lambda o: o[0])
        i = option[1]
        jumped += 1

    return jumped


if __name__ == "__main__":
    assert jump(nums=[2, 3, 1, 1, 4]) == 2
    assert jump(nums=[2, 3, 0, 1, 4]) == 2
    assert jump(nums=[2, 1]) == 1
    assert jump(nums=[3, 2, 1]) == 1
    assert jump(nums=[1, 2, 1, 1, 1]) == 3
