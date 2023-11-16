"""
# 746
Easy
Min Cost Climbing Stairs

https://leetcode.com/problems/min-cost-climbing-stairs

You are given an integer array cost where cost[i] is the cost of ith step on a staircase.
Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.
Return the minimum cost to reach the top of the floor.

Example 1:
Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.

Example 2:
Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.

Constraints:
2 <= cost.length <= 1000
0 <= cost[i] <= 999
"""


def min_cost_climbing_stairs(cost: list[int]) -> int:
    top = len(cost)

    # ex: cost = [10, 15, 20]
    # Store first and second cost in to dp list. ex: [10, 15, 0]
    # 因為一次可以走一階或兩階, 到達一二階所需的花費即自己該層的花費
    dp = [cost[ci] if ci <= 1 else 0 for ci in range(top)]

    # 要走到從三階開始以後的任一階, 必定會經過前兩階其中一階
    # 所以找出前兩階較小的 cost 並加上當下要走到的 cost 即為走到此階所需的費用
    for i in range(2, len(cost)):
        dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]

    # 最後解答到走到的頂層為 index = len(cost) (即超過 cost 的後一個元素)
    return min(dp[top - 2], dp[top - 1])


if __name__ == "__main__":
    assert min_cost_climbing_stairs([10, 15, 20]) == 15
    assert min_cost_climbing_stairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6
