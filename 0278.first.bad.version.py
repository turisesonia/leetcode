"""
# 278
Easy
First Bad Version

https://leetcode.com/problems/first-bad-version/

You are a product manager and currently leading a team to develop a new product.
Unfortunately, the latest version of your product fails the quality check.
Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad.
Implement a function to find the first bad version.
You should minimize the number of calls to the API.

Example 1:
Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.

Example 2:
Input: n = 1, bad = 1
Output: 1

Constraints:

1 <= bad <= n <= 231 - 1
"""


def isBadVersion(version: int) -> bool:
    global bad_version

    return version >= bad_version


def first_bad_version(n: int) -> int:
    """
    用 Binary search 解, 但在移動起始指標時,  需要將起始指標 + 1

    ex:
    bad version = 4
    input version = 5

    versions = [1, 2, 3, 4, 5]
    low = 1, high = 5, target = 4

    # round 1
    mid = (1 + 5) // 2 = 3

    3 不是錯誤的版本
    所以將 low 指摽移動到 3 + 1, (low set to 4)
    low = 4, high = 5, target = 4

    # round 2
    mid = (4 + 5) // 2 = 4
    4 是錯誤的版本, 移動結尾指標到 4, (high set to 4)
    low = 4, high = 4, target = 4

    此時 low = high, 找到 target, 結束 while 迴圈
    """
    low, high = 1, n

    while low < high:
        mid = (low + high) // 2

        bad = isBadVersion(mid)

        if not bad:
            low = mid + 1
        else:
            high = mid

    return low


if __name__ == "__main__":
    bad_version = 1
    assert first_bad_version(1) == 1

    bad_version = 4
    assert first_bad_version(5) == 4

    bad_version = 1
    assert first_bad_version(2) == 1

    bad_version = 1702766719
    assert first_bad_version(2126753390) == 1702766719
