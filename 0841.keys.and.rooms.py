"""
# 841
Medium
Keys and Rooms

https://leetcode.com/problems/keys-and-rooms

There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0.
Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.

When you visit a room, you may find a set of distinct keys in it.
Each key has a number on it, denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.

Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, return true if you can visit all the rooms, or false otherwise.

Example 1:
Input: rooms = [[1],[2],[3],[]]
Output: true
Explanation:
We visit room 0 and pick up key 1.
We then visit room 1 and pick up key 2.
We then visit room 2 and pick up key 3.
We then visit room 3.
Since we were able to visit every room, we return true.

Example 2:
Input: rooms = [[1,3],[3,0,1],[2],[0]]
Output: false
Explanation: We can not enter room number 2 since the only key that unlocks it is in that room.


Constraints:
n == rooms.length
2 <= n <= 1000
0 <= rooms[i].length <= 1000
1 <= sum(rooms[i].length) <= 3000
0 <= rooms[i][j] < n
All the values of rooms[i] are unique.
"""


def can_visit_all_rooms(rooms: list[list[int]]) -> bool:
    """
    DFS in stack version

    Args:
        rooms (list[list[int]]):

    Returns:
        bool:
    """
    # According to the question, room 0 is unlocked, so the variable "visited" start from 1
    visited = 1
    keys = {0}

    # "holds" represents how many room keys we hold
    holds = [num for num in rooms[0] if num not in keys]

    while holds:
        k = holds.pop(0)

        if k in keys:
            continue

        keys.add(k)
        visited += 1

        for k_ in rooms[k]:
            if k_ not in keys:
                holds.append(k_)

    return visited == len(rooms)


def can_visit_all_rooms(rooms: list[list[int]]) -> bool:
    """
    DFS in recursive version

    Args:
        rooms (list[list[int]]):

    Returns:
        bool:
    """
    visited = {0}

    def dfs(idx: int):
        for key in rooms[idx]:
            if key not in visited:
                visited.add(key)
                dfs(key)

    dfs(0)

    return len(visited) == len(rooms)


if __name__ == "__main__":
    assert can_visit_all_rooms([[1], [2], [3], []])
    assert not can_visit_all_rooms([[1, 3], [3, 0, 1], [2], [0]])
    assert can_visit_all_rooms([[1, 2], [2, 1], [1]])
