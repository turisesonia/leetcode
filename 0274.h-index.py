"""
# 274
Medium
H-Index

https://leetcode.com/problems/h-index

Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.

According to the definition of h-index on Wikipedia:
The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.

Example 1:
Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.

Example 2:
Input: citations = [1,3,1]
Output: 1

Constraints:
* n == citations.length
* 1 <= n <= 5000
* 0 <= citations[i] <= 1000

Reference
H-Index: http://tul.blog.ntu.edu.tw/archives/2485
"""


def h_index(citations: list[int]) -> int:
    """
    H-index
    有 h 篇文章至少被引用 h 次
    """

    h_index = 0

    # reverse citations list
    citations.sort(reverse=True)

    for idx, cit in enumerate(citations):
        # ith paper
        ith = idx + 1

        # citation bigger than the count of papers
        if cit >= ith:
            h_index += 1

    return h_index


if __name__ == "__main__":
    assert h_index(citations=[3, 0, 6, 1, 5]) == 3
    assert h_index(citations=[1, 3, 1]) == 1
