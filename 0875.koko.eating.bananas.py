"""
# 875
Medium
Koko Eating Bananas

https://leetcode.com/problems/koko-eating-bananas

Koko loves to eat bananas.
There are n piles of bananas, the ith pile has piles[i] bananas.
The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k.
Each hour, she chooses some pile of bananas and eats k bananas from that pile.
If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.


Example 1:
Input: piles = [3,6,7,11], h = 8
Output: 4

Example 2:
Input: piles = [30,11,23,4,20], h = 5
Output: 30

Example 3:
Input: piles = [30,11,23,4,20], h = 6
Output: 23


Constraints:

1 <= piles.length <= 104
piles.length <= h <= 109
1 <= piles[i] <= 109
"""
from math import ceil


def min_eating_speed(piles: list[int], h: int) -> int:
    left, right = ceil(sum(piles) / h), max(piles)
    while left != right:
        mid = (left + right) // 2
        print(left, mid, right)

        use_hours = 0
        for pile in piles:
            use_hours += ceil(pile / mid)

        if use_hours <= h:
            right = mid
        else:
            left = left + 1

    print(left)
    return left


if __name__ == "__main__":
    # assert min_eating_speed([3, 6, 7, 11], h=8) == 4
    # assert min_eating_speed([30, 11, 23, 4, 20], h=5) == 30
    # assert min_eating_speed([30, 11, 23, 4, 20], h=6) == 23
    assert min_eating_speed([1000000000, 1000000000], h=3)
