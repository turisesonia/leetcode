"""
# 56
Medium
Merge Intervals

https://leetcode.com/problems/merge-intervals/description/

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
"""


def merge(intervals: list[list[int]]) -> list[list[int]]:
    if len(intervals) <= 1:
        return intervals

    intervals.sort(key=lambda i: i[0])

    res = []
    prev = None

    for inter in intervals:
        if not prev:
            prev = inter
            continue

        st = inter[0]
        ed = inter[1]

        if st > prev[1]:
            res.append(prev)
            prev = inter
        else:
            st = prev[0] if prev[0] < st else st
            ed = prev[1] if prev[1] > ed else ed
            prev = [st, ed]

    res.append(prev)

    return res


if __name__ == "__main__":
    assert merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert merge([[1, 4], [4, 5]]) == [[1, 5]]
    assert merge([[1, 4], [0, 4]]) == [[0, 4]]
    assert merge([[1, 4], [0, 1]]) == [[0, 4]]
    assert merge([[1, 4], [2, 3]]) == [[1, 4]]
