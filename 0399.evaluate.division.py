"""
# 399
Medium
Evaluate Division

https://leetcode.com/problems/evaluate-division

You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.
You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.
Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.
Note: The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.

Example 1:
Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation:
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
note: x is undefined => -1.0

Example 2:
Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]

Example 3:
Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]

Constraints:
- 1 <= equations.length <= 20
- equations[i].length == 2
- 1 <= Ai.length, Bi.length <= 5
- values.length == equations.length
- 0.0 < values[i] <= 20.0
- 1 <= queries.length <= 20
- queries[i].length == 2
- 1 <= Cj.length, Dj.length <= 5
- Ai, Bi, Cj, Dj consist of lower case English letters and digits.
"""

from typing import List


def calc_equation(
    equations: List[List[str]], values: List[float], queries: List[List[str]]
) -> List[float]:
    """
    Ex: [[a, b], [b, c]], [2, 3]
    先理解出 a / b = 2 轉換成 Graph 即為 a -> b 方向的距離為 2
    反過來 b / a = 1 / 2 即為 b -> a 方向的距離為 1 / 2

    - b / c = 3
      - b -> c = 3
      - c -> b = 1 / 3

    根據上面的結果，可以得出 a -> c = a -> b -> c
    此段距離長度就為 (a -> b) * (b -> c) = 2 * 3 = 6
    """
    result = []

    # 依照參數找出各點互相往返的距離
    paths = {}
    for idx, equ in enumerate(equations):
        start, end = equ
        value = values[idx]

        if start not in paths:
            paths[start] = []

        if end not in paths:
            paths[end] = []

        paths[start].append((end, value))
        paths[end].append((start, 1 / value))

    for query in queries:
        from_, to_ = query

        # 如果有起點或終點都不在 paths 內，代表路徑一定不存在
        if from_ not in paths or to_ not in paths:
            result.append(-1)
            continue

        # 起點終點相同
        if from_ == to_:
            result.append(1)
            continue

        # 記錄已經訪問過的位置
        visited = {from_}

        # DFS (現在的位置, 距離)
        stack = [(from_, 1)]
        while stack:
            n, value = stack.pop()

            # 找到終點
            if n == to_:
                result.append(value)
                break

            # 判斷與現在節點有連接且尚未走過的節點
            for path in paths[n]:
                des, val = path

                if des not in visited:
                    visited.add(des)
                    stack.append((des, value * val))
        else:
            # 全部都走過但是無法到達終點的情況
            result.append(-1)

    return result


if __name__ == "__main__":
    assert calc_equation(
        equations=[["a", "b"], ["b", "c"]],
        values=[2.0, 3.0],
        queries=[["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]],
    ) == [6.00000, 0.50000, -1.00000, 1.00000, -1.00000]

    assert calc_equation(
        equations=[["a", "b"], ["b", "c"], ["bc", "cd"]],
        values=[1.5, 2.5, 5.0],
        queries=[["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]],
    ) == [3.75000, 0.40000, 5.00000, 0.20000]

    assert calc_equation(
        equations=[["a", "b"]],
        values=[0.5],
        queries=[["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]],
    ) == [0.50000, 2.00000, -1.00000, -1.00000]

    assert calc_equation(
        equations=[["a", "e"], ["b", "e"]],
        values=[4.0, 3.0],
        queries=[["a", "b"], ["e", "e"], ["x", "x"]],
    ) == [4 / 3, 1.00000, -1.00000]

    assert calc_equation(
        equations=[["a", "b"], ["c", "d"]],
        values=[1.0, 1.0],
        queries=[["a", "c"], ["b", "d"], ["b", "a"], ["d", "c"]],
    ) == [-1.00000, -1.00000, 1.00000, 1.00000]
