"""
# 492
Easy
Construct the Rectangle

https://leetcode.com/problems/construct-the-rectangle/

A web developer needs to know how to design a web page's size. So, given a specific rectangular web page's area,
your job by now is to design a rectangular web page, whose length L and width W satisfy the following requirements:

1. The area of the rectangular web page you designed must equal to the given target area.
2. The  width W should not be larger than the length L, which means L >= W.
3. The difference between length L and width W should be as small as possible.

Return an array [L, W] where L and W are the length and width of the web page you designed in sequence.

Example 1:
Input: area = 4
Output: [2, 2]
Explanation: The target area is 4, and all the possible ways to construct it are [1,4], [2,2], [4,1].
But according to requirement 2, [1,4] is illegal; according to requirement 3,  [4,1] is not optimal compared to [2,2]. So the length L is 2, and the width W is 2.

Example 2:
Input: area = 37
Output: [37, 1]
Example 3:

Input: area = 122122
Output: [427, 286]

Constraints:
1 <= area <= 10^7
"""


def construct_rectangle(area: int) -> list[int]:
    """
    要找到最小的長寬差異就是用 area 計算出正方形
    L * M = area when L = M, L - M == 0

    用上面的公式找出答案
    """
    hm = {}
    sqrt = int(area**0.5)

    for w in range(1, sqrt + 1):
        if area % w == 0:
            l = int(area / w)

            hm[l - w] = [l, w]

    key = min(hm.keys())

    return hm[key]


def construct_rectangle(area: int) -> list[int]:
    sqrt = int(area**0.5)
    for w in range(sqrt, 0, -1):
        if area % w == 0:
            return [area // w, w]


if __name__ == "__main__":
    assert construct_rectangle(4) == [2, 2]
    assert construct_rectangle(37) == [37, 1]
    assert construct_rectangle(122122) == [427, 286]
