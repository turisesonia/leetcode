"""
# 435
Medium
Non-overlapping Intervals

https://leetcode.com/problems/non-overlapping-intervals

Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Example 1:
Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

Example 2:
Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.

Example 3:
Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.

Constraints:
* 1 <= intervals.length <= 10^5
* intervals[i].length == 2
* -5 * 10^4 <= starti < endi <= 5 * 10^4

Hint:

https://assets.leetcode.com/users/images/515fa83b-44c2-4c42-8ef5-d41c7942ec32_1653774876.169032.jpeg

"""


def erase_overlap_intervals(intervals: list[list[int]]) -> int:
    # Sort the intervals by the firs element of each item in intervals
    intervals = sorted(intervals, key=lambda item: item[0])

    removed = 0

    # Use first item as start inverval
    current = intervals[0]

    for inter in intervals[1:]:
        start, end = inter

        if start >= current[1]:
            # not overlapping, change "current" to current interval
            current = inter
        else:
            # overlapping
            removed += 1

            if current[1] > end:
                current = inter

    return removed


if __name__ == "__main__":
    assert erase_overlap_intervals(intervals=[[1, 2], [2, 3], [3, 4], [1, 3]]) == 1
    assert erase_overlap_intervals(intervals=[[1, 2], [1, 2], [1, 2]]) == 2
    assert erase_overlap_intervals(intervals=[[1, 2], [2, 3]]) == 0
    assert erase_overlap_intervals(intervals=[[1, 100], [11, 22], [1, 11], [2, 12]]) == 2
    assert (
        erase_overlap_intervals(
            intervals=[
                [-52, 31],
                [-73, -26],
                [82, 97],
                [-65, -11],
                [-62, -49],
                [95, 99],
                [58, 95],
                [-31, 49],
                [66, 98],
                [-63, 2],
                [30, 47],
                [-40, -26],
            ]
        )
        == 7
    )
