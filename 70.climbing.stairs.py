"""
# 70
Climbing Stairs
Easy

https://leetcode.com/problems/climbing-stairs/

You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Constraints:

1 <= n <= 45
"""


# v1
def climb_stairs(n: int) -> int:
    data = [1, 2]

    if n in data:
        return n

    for i in range(n):
        if i in (0, 1):
            continue

        data.append(data[i - 2] + data[i - 1])

    return data.pop()


# v2
def climb_stairs(n: int) -> int:
    data = [0, 1, 2]

    # 因前面已經宣告三個數字, 從 3 開始
    for i in range(3, n + 1):
        data.append(data[i - 2] + data[i - 1])

    return data[n]


def climb_stairs(n: int):
    """
    Answer from leetcode
    """
    # [0, 1, 1, 2, 3, 5, 8, 13, ...]
    idx_0, idx_1 = 0, 1

    for _ in range(n):
        idx_0, idx_1 = idx_1, idx_0 + idx_1

    return idx_1


if __name__ == "__main__":
    assert climb_stairs(1) == 1
    assert climb_stairs(2) == 2
    assert climb_stairs(3) == 3
    assert climb_stairs(4) == 5
    assert climb_stairs(5) == 8
    assert climb_stairs(6) == 13
