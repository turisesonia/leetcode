"""
# 1971
Easy
Find if Path Exists in Graph

https://leetcode.com/problems/find-if-path-exists-in-graph/description/

There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive).
The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi.
Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex source to vertex destination.
Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise.

Example 1:
Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
Output: true
Explanation: There are two paths from vertex 0 to vertex 2:
- 0 → 1 → 2
- 0 → 2

Example 2:
Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
Output: false
Explanation: There is no path from vertex 0 to vertex 5.


Constraints:
- 1 <= n <= 2 * 105
- 0 <= edges.length <= 2 * 105
- edges[i].length == 2
- 0 <= ui, vi <= n - 1
- ui != vi
- 0 <= source, destination <= n - 1
- There are no duplicate edges.
- There are no self edges.
"""


def valid_path(n: int, edges: list[list[int]], source: int, destination: int) -> bool:
    if n <= 1:
        return True

    # get all path
    paths = {}
    for edge in edges:
        n1, n2 = edge

        if n1 in paths:
            paths[n1].add(n2)
        else:
            paths[n1] = {n2}

        if n2 in paths:
            paths[n2].add(n1)
        else:
            paths[n2] = {n1}

    # store every node visited
    visited = [True if i == source else False for i in range(n)]

    # DFS
    stack = [source]
    while stack:
        current = stack.pop()

        for node in paths.get(current, []):
            if node == destination:
                return True

            if not visited[node]:
                visited[node] = True
                stack.append(node)

    return False


if __name__ == "__main__":
    assert valid_path(n=1, edges=[], source=0, destination=0)
    assert valid_path(n=3, edges=[[0, 1], [1, 2], [2, 0]], source=0, destination=2)
    assert not valid_path(
        n=6, edges=[[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], source=0, destination=5
    )
    assert not valid_path(
        n=10,
        edges=[[2, 9], [7, 8], [5, 9], [7, 2], [3, 8], [2, 8], [1, 6], [3, 0], [7, 0], [8, 5]],
        source=1,
        destination=0,
    )
