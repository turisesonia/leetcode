"""
# 198
Medium
House Robber

https://leetcode.com/problems/house-robber

You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 400
"""


def rob(nums: list[int]) -> int:
    houses = len(nums)

    # 記錄各房子最多可以搶到多少錢
    # 因不可以搶相鄰房子的錢，所以前兩間只能有自己的金額
    dp = [nums[i] if i <= 1 else 0 for i in range(houses)]

    # 後續能搶到的錢為, 跳過前一間後找最大值
    for j in range(2, houses):
        dp[j] = nums[j] + max(dp[: j - 1])

    return max(dp)


if __name__ == "__main__":
    assert rob([1, 2, 3, 1]) == 4
    assert rob([2, 7, 9, 3, 1]) == 12
    assert rob([2, 1, 1, 2]) == 4
