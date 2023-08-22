"""
# 401
Easy
Binary Watch

https://leetcode.com/problems/binary-watch/

A binary watch has 4 LEDs on the top to represent the hours (0-11), and 6 LEDs on the bottom to represent the minutes (0-59).
Each LED represents a zero or one, with the least significant bit on the right.

For example, the below binary watch reads "4:51".

Given an integer turnedOn which represents the number of LEDs that are currently on (ignoring the PM), return all possible times the watch could represent.
You may return the answer in any order.

The hour must not contain a leading zero.
For example, "01:00" is not valid. It should be "1:00".

The minute must be consist of two digits and may contain a leading zero.
For example, "10:2" is not valid. It should be "10:02".

Example 1:
Input: turnedOn = 1
Output: ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]

Example 2:
Input: turnedOn = 9
Output: []

Constraints:

0 <= turnedOn <= 10
"""


def read_binary_watch(turnedOn: int) -> list[str]:
    """
    hour:
    8 4 2 1

    minute:
    32 16 8 4 2 1
    """

    res = []
    # hours:   0 ~ 11
    # minutes: 0 ~ 59
    for h in range(12):
        for m in range(60):
            # Count the number of times "1" appers in both the hours and minutes binary strings, and the result should be equals to turnedOn.
            if bin(h).count("1") + bin(m).count("1") == turnedOn:
                m = str(m).zfill(2)
                res.append(f"{h}:{m}")

    return res


if __name__ == "__main__":
    assert set(read_binary_watch(1)) == {
        "0:01",
        "0:02",
        "0:04",
        "0:08",
        "0:16",
        "0:32",
        "1:00",
        "2:00",
        "4:00",
        "8:00",
    }
    assert set(read_binary_watch(9)) == set()
