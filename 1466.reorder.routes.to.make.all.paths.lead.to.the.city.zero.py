"""
# 1466
Medium
Reorder Routes to Make All Paths Lead to the City Zero

https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/?envType=study-plan-v2&envId=leetcode-75

There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two different cities (this network form a tree).
Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.

Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.
This year, there will be a big event in the capital (city 0), and many people want to travel to this city.
Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.

It's guaranteed that each city can reach city 0 after reorder.

Example 1:

https://assets.leetcode.com/uploads/2020/05/13/sample_1_1819.png

Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
Output: 3
Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).

Example 2:

https://assets.leetcode.com/uploads/2020/05/13/sample_2_1819.png

Input: n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
Output: 2
Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).

Example 3:
Input: n = 3, connections = [[1,0],[2,0]]
Output: 0

Constraints:

- 2 <= n <= 5 * 10^4
- connections.length == n - 1
- connections[i].length == 2
- 0 <= ai, bi <= n - 1
- ai != bi
"""

from typing import List


def min_reorder(n: int, connections: List[List[int]]) -> int:
    # ! Time Limit Exceeded
    reorder = 0
    tmp = []
    destinations = []

    for conn in connections:
        a, b = conn[0], conn[1]

        if a == 0:
            conn[0] = b
            conn[1] = a
            reorder += 1

            destinations.append(b)
            continue

        if b == 0:
            destinations.append(a)
            continue

        if a in destinations and b not in destinations:
            conn[0] = b
            conn[1] = a
            reorder += 1

            destinations.append(b)

        elif b in destinations and a not in destinations:
            destinations.append(a)

        else:
            tmp.append(conn)

    while tmp:
        conn = tmp.pop(0)
        a, b = conn[0], conn[1]

        if a in destinations and b not in destinations:
            conn[0] = b
            conn[1] = a
            reorder += 1

            destinations.append(b)

        elif b in destinations and a not in destinations:
            destinations.append(a)

        else:
            tmp.append(conn)

    return reorder


def min_reorder(n: int, connections: List[List[int]]) -> int:
    """
    從 root node (從 0 開始) 開始遍歷所有 child node
    只要取到的方向 (ex: 0 -> 1 -> 2 ... ) 與 connections 的方向一樣, 代表就是需要轉向的路徑

    Ex: connections = [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]

          0           0 <- 1 -> 3
         / \          ^         ^
        1   4         |         |
       /     \        4 -> 5    2
      3       5
     /
    2

    根據 connections 可以產生出"正向"與"反向"路徑的兩個 hash map
    direct  = {0: [1], 1: [3], [2]: 3, 4: [0, 5]}
    reverse = {1: [0], 3: [1, 2], 0: [4], 5: [4]}

    接下來對轉成樹的 node 做 root -> end 的 DFS
    只要走的方向在存在於 direct 內, 代表就是需要轉向的路徑 (因為題目要可以從所有的 child node 走回 zero node)
    """
    count = 0
    direct = {}
    reverse = {}

    for conn in connections:
        from_, to_ = conn[0], conn[1]

        if from_ in direct:
            direct[from_].append(to_)
        else:
            direct[from_] = [to_]

        if to_ in reverse:
            reverse[to_].append(from_)
        else:
            reverse[to_] = [from_]

    visited = [False if i > 0 else True for i in range(n)]

    # DFS
    stack = [0]
    while stack:
        num = stack.pop()

        for city in direct.get(num, []):
            if not visited[city]:
                count += 1
                visited[city] = True
                stack.append(city)

        for city in reverse.get(num, []):
            if not visited[city]:
                stack.append(city)
                visited[city] = True

    return count


if __name__ == "__main__":
    assert min_reorder(n=6, connections=[[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]) == 3
    assert min_reorder(n=5, connections=[[1, 0], [1, 2], [3, 2], [3, 4]]) == 2
    assert min_reorder(n=3, connections=[[1, 0], [2, 0]]) == 0
    assert min_reorder(n=5, connections=[[4, 3], [2, 3], [1, 2], [1, 0]]) == 2
