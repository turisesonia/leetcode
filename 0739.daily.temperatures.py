"""
# 739
Medium
Daily Temperatures

https://leetcode.com/problems/daily-temperatures/description

Given an array of integers temperatures represents the daily temperatures,
return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature.
If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]

Constraints:
1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100
"""


def daily_temperatures(temperatures: list[int]) -> list[int]:
    """
    Broute-force solution
    # ! Time Limit Exceeded

    O(n**2)
    """
    ans = []
    for i, temp in enumerate(temperatures):
        for j, temp_ in enumerate(temperatures):
            if j <= i:
                continue

            if temp_ > temp:
                ans.append(j - i)
                break
        else:
            ans.append(0)

    return ans


def daily_temperatures(temperatures: list[int]) -> list[int]:
    """
    Stack solution
    O(2n)
    """
    ans = []
    stack = []
    hm = {}

    for idx in range(len(temperatures)):
        t = temperatures[idx]

        while stack and t > stack[-1][1]:
            date_temp = stack.pop()
            hm[date_temp] = idx

        stack.append((idx, t))

    for date, temp in enumerate(temperatures):
        warmer_date = hm.get((date, temp))

        if warmer_date:
            ans.append(warmer_date - date)
        else:
            ans.append(0)

    return ans


if __name__ == "__main__":
    assert daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
    assert daily_temperatures([30, 40, 50, 60]) == [1, 1, 1, 0]
    assert daily_temperatures([30, 60, 90]) == [1, 1, 0]
