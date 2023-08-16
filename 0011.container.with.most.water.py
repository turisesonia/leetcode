"""
# 11
Medium
Container With Most Water

https://leetcode.com/problems/container-with-most-water/

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation:
The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
"""
from typing import List


# v1 把每個組合都找出來比較大小, 資料量大就會非常慢  不合格
def max_area(height: List[int]) -> int:
    length = current = len(height)

    result = 0

    while current > 0:
        btm = current - 1

        if btm == 0:
            break

        for i in range(length - current + 1):
            ph = height[i : current + i]

            hei = min(ph[0], ph[-1])
            amount = hei * btm

            if amount > result:
                result = amount

            print(f"{hei} * {btm} = {amount}")
        print("---", btm)

        current -= 1

    return result


# v2 參考 leetcode 討論區後的解法
def max_area(height: List[int]) -> int:
    """
    不要用容器的方式去思考,
    這題就是找出兩個元素包含的矩形面積, 高度為兩元素的最小值, 寬度為兩元素的距離

    解題流程
    ex: [1, 8, 6, 2, 5, 4, 8, 3, 7]
    宣告兩個變數當位置指標 left, right
    left 為 list 開頭 index ( 0 )
    right 為 list 最後位置的 index ( len(height) - 1 )

    矩形高度 = left, right 這兩個位置取最小值 (min(height[l], height[r]))
    矩形寬度 = right - left

    1. 計算面積
    比較 height[l] 及 height[r] 的值, 找出較小的及為矩形高度
    計算矩形面積後跟 result 比較交將較大的值存下來

    2. 移動位置指針
    移動值較小的方向的指針

    如果 height[left] 較小即 left 右移 (left += 1)
    如果 height[right] 較小即 right 左移 (right -= 1)

    一直計算直到兩個位置相碰停止
    """
    length = len(height)

    l = 0
    r = length - 1

    result = 0

    while r > l:
        hei = min(height[l], height[r])
        width = r - l

        area = hei * width

        if area > result:
            result = area

        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return result


if __name__ == "__main__":
    assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert max_area([1, 1]) == 1
