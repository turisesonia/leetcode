"""
# 605
Easy
Can Place Flowers

https://leetcode.com/problems/can-place-flowers

You have a long flowerbed in which some of the plots are planted, and some are not.
However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.


Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: false

Constraints:

1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length
"""
from typing import List


def can_place_flowers(flowerbed: List[int], n: int) -> bool:
    l = len(flowerbed)
    i = 0

    while i < l:
        num = flowerbed[i]

        # 1. 鄰近兩格都不行, 所以判斷到該位置為 1 (有種花), 直接跳過下一個去檢查下下個位置
        if num == 1:
            i += 2
            continue

        # 2. 因為從最左至右, 不需檢查左邊的位置, 所以之後只需要看右邊的位置是否為 0 或現在是最後一個位置
        next_ = i + 1
        if (next_ >= l) or (next_ <= l and flowerbed[next_] == 0):
            n -= 1
            i += 2
        else:
            # 同 1 的判斷
            i += 3

    return n == 0


if __name__ == "__main__":
    assert can_place_flowers([1, 0, 0, 0, 1], 1) == True
    assert can_place_flowers([1, 0, 0, 0, 1], 2) == False
    assert can_place_flowers([1, 0, 0, 0, 0, 1], 2) == False
    assert can_place_flowers([0, 0, 1, 0, 0], 1) == True
