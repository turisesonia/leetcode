"""
# 455
Easy
Assign Cookies

https://leetcode.com/problems/assign-cookies/

Assume you are an awesome parent and want to give your children some cookies.
But, you should give each child at most one cookie.

Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with; and each cookie j has a size s[j].
If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content.
Your goal is to maximize the number of your content children and output the maximum number.

Example 1:
Input: g = [1,2,3], s = [1,1]
Output: 1
Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3.
And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.
You need to output 1.

Example 2:
Input: g = [1,2], s = [1,2,3]
Output: 2
Explanation: You have 2 children and 3 cookies. The greed factors of 2 children are 1, 2.
You have 3 cookies and their sizes are big enough to gratify all of the children,
You need to output 2.

Constraints:

1 <= g.length <= 3 * 10^4
0 <= s.length <= 3 * 10^4
1 <= g[i], s[j] <= 2^31 - 1
"""

# Exceeded time limit
# def find_content_children(g: list[int], s: list[int]) -> int:
#     max_ = 0
#     hm = {}

#     for child in g:
#         hm[child] = hm.get(child, 0) + 1

#     s.sort(reverse=True)

#     for cookie in s:
#         while cookie > 0:
#             if hm.get(cookie, 0) > 0:
#                 max_ += 1
#                 hm[cookie] -= 1
#                 break
#             else:
#                 cookie -= 1

#     return max_


def find_content_children(g: list[int], s: list[int]) -> int:
    """
    Greedy Algorithm

    1. 將小孩和餅乾由小至大排序
    2. 從最小需求的小孩和最小的餅乾開始比對
    3. 如果餅乾可以滿足小孩, 小孩和餅乾都往下一個比對
    4. 如果餅乾大小無法滿足當下小孩的需求, 則檢查下一個餅乾直到可以滿足小孩
    """
    g.sort()
    s.sort()

    child, cookie = 0, 0

    while child < len(g) and cookie < len(s):
        if g[child] <= s[cookie]:
            child += 1

        cookie += 1

    return child


if __name__ == "__main__":
    assert find_content_children([1, 2, 3], [1, 1]) == 1
    assert find_content_children([1, 2], [1, 2, 3]) == 2
