"""
# 547
Medium
Number of Provinces

https://leetcode.com/problems/number-of-provinces/description/?envType=study-plan-v2&envId=leetcode-75

There are n cities.
Some of them are connected, while some are not.
If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.



Example 1:
Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2

Example 2:
Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3

Constraints:
1 <= n <= 200
n == isConnected.length
n == isConnected[i].length
isConnected[i][j] is 1 or 0.
isConnected[i][i] == 1
isConnected[i][j] == isConnected[j][i]
"""

from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """
        DFS recursive version.

        Visit each element in the list one by one, with a priority to find elements connected to the current element,
        and store the visited elements to prevent revisiting.

        Args:
            isConnected (List[List[int]]): _description_

        Returns:
            int: _description_
        """
        # the province count, max value is len(isConnected)
        province = 0

        # visited city index
        visited = set()

        def dfs(idx: int):
            visited.add(idx)

            city = isConnected[idx]

            for i, connected in enumerate(city):
                # if have not visited city and it is connected to the current city
                if i not in visited and connected:
                    dfs(i)

        # visit every not connected city
        for idx in range(len(isConnected)):
            if idx not in visited:
                dfs(idx)
                province += 1

        return province


if __name__ == "__main__":
    solution = Solution()

    prov = solution.findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]])
    assert prov == 2

    prov = solution.findCircleNum([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    assert prov == 3

    prov = solution.findCircleNum(
        [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
    )
    assert prov == 1

    prov = solution.findCircleNum(
        [
            [1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
            [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1],
            [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        ]
    )
    assert prov == 3
