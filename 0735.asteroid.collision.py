"""
# 735
Medium
Asteroid Collision

https://leetcode.com/problems/asteroid-collision

We are given an array asteroids of integers representing asteroids in a row.
給定一個 array, 裡面包含一串數字代表小行星在同一列上

For each asteroid,
對於裡面每一個小行星
the absolute value represents its size,
數字的絕對值代表行星的大小
and the sign represents its direction (positive meaning right, negative meaning left).
且其符號代表他移動的方向 (正代表向右移動, 負代表向左移動)
Each asteroid moves at the same speed.
所有小行星的移動速度都一樣

Find out the state of the asteroids after all collisions.
找出所有行星的相撞後的狀態
If two asteroids meet, the smaller one will explode. If both are the same size, both will explode.
如果兩個小行星相遇, 較小的行星會爆炸, 如果大小一樣, 則兩個行星都爆炸
Two asteroids moving in the same direction will never meet.
往相同方向移動的小行星永遠都不會相遇

Example 1:
Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

Example 2:
Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.

Example 3:
Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.

Constraints:
2 <= asteroids.length <= 104
-1000 <= asteroids[i] <= 1000
asteroids[i] != 0
"""
from typing import List


def asteroid_collision(asteroids: List[int]) -> List[int]:
    # 建立一個 list 當成 stack 由左至右存放小行星
    stack = []

    for ast in asteroids:
        # 只有在 "左邊的行星向右移動" 且 "右邊的行星向左移動" 才會相遇
        # 即 left number > 0 and right number < 0
        # 除此之外都不會相遇直接把數字加入 stack
        while len(stack) > 0 and stack[-1] > 0 > ast:
            # 當相遇時數字較大時, 要移出較小的那個
            if abs(ast) > stack[-1]:
                stack.pop()

            # 相遇時數字一樣
            elif abs(ast) == stack[-1]:
                stack.pop()
                break

            # 相遇數字較小
            else:
                break

        else:
            stack.append(ast)

    return stack


if __name__ == "__main__":
    assert asteroid_collision([5, 10, -5]) == [5, 10]
    assert asteroid_collision([8, -8]) == []
    assert asteroid_collision([10, 2, -5]) == [10]
    assert asteroid_collision([-2, -1, 1, 2]) == [-2, -1, 1, 2]
    assert asteroid_collision([5, 3, -5]) == []
