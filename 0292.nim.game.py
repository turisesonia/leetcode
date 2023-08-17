"""
# 292
Easy
Nim Game

https://leetcode.com/problems/nim-game/

You are playing the following Nim Game with your friend:

Initially, there is a heap of stones on the table.
You and your friend will alternate taking turns, and you go first.
On each turn, the person whose turn it is will remove 1 to 3 stones from the heap.
The one who removes the last stone is the winner.
Given n, the number of stones in the heap, return true if you can win the game assuming both you and your friend play optimally, otherwise return false.

Example 1:
Input: n = 4
Output: false
Explanation: These are the possible outcomes:
1. You remove 1 stone. Your friend removes 3 stones, including the last stone. Your friend wins.
2. You remove 2 stones. Your friend removes 2 stones, including the last stone. Your friend wins.
3. You remove 3 stones. Your friend removes the last stone. Your friend wins.
In all outcomes, your friend wins.

Example 2:
Input: n = 1
Output: true

Example 3:
Input: n = 2
Output: true

Constraints:
1 <= n <= 2^31 - 1

a: you, b: frirend

You go first to remove rocks.
so, if the quantity of rocks is multiple of 4 you will lose anyway
"""


def can_win_nim(n: int) -> bool:
    if n <= 3:
        return True

    for i in range(1, 4):
        if (n - i) % 4 == 0:
            return True

    return False


def can_win_nim(n: int) -> bool:
    # when it's your turn and the qty of rocks is mutliple of 4, you will lose anyway.
    return n % 4 != 0


if __name__ == "__main__":
    assert can_win_nim(1)
    assert can_win_nim(2)
    assert not can_win_nim(4)
    assert can_win_nim(5)
