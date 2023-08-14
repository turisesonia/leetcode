"""
# 231
Easy
Power of Two

https://leetcode.com/problems/power-of-two/

Given an integer n, return true if it is a power of two. Otherwise, return false.
An integer n is a power of two, if there exists an integer x such that n == 2x.

Example 1:
Input: n = 1
Output: true
Explanation: 2**0 = 1

Example 2:
Input: n = 16
Output: true
Explanation: 2**4 = 16

Example 3:
Input: n = 3
Output: false

Constraints:

-231 <= n <= 231 - 1

Follow up: Could you solve it without loops/recursion?
"""


def is_power_of_two(n: int) -> bool:
    """
    直接做 2 次方去比較是否等於 n
    當 2**x > n , 代表 n 不是 power of 2
    """
    x = 0

    while 2**x <= n:
        if 2**x == n:
            return True

        x += 1
    return False


"""
下面兩個解法用 binary system 解決問題
當一個數 n 要是 2 的次方, 代表此 n 在二進制內只會有一個 1
Example:
      1 => 1  (2^0)
     10 => 2  (2^1)
    100 => 4  (2^2)
   1000 => 8  (2^3)
  10000 => 16 (2^4)
 100000 => 32 (2^5)
1000000 => 64 (2^6)

且 n - 1 時, 都會差一個位數並且數字均為 1
      0 => 0  (2^0 - 1)
     01 => 1  (2^1 - 1)
    011 => 3  (2^2 - 1)
   0111 => 7  (2^3 - 1)
  01111 => 15 (2^4 - 1)
 011111 => 31 (2^5 - 1)
0111111 => 63 (2^6 - 1)

所以當 n 是 2 的次方時, 做 bit and 會等於 0
n & (n - 1) == 0
"""


def is_power_of_two(n: int) -> bool:
    if n < 1:
        return False

    s = f"{abs(n):b}"

    t = 0
    for i in s:
        t += int(i)

    return t == 1


def is_power_of_two(n: int) -> bool:
    return n > 0 and (n & (n - 1)) == 0


if __name__ == "__main__":
    assert is_power_of_two(1)
    assert is_power_of_two(16)
    assert not is_power_of_two(3)
    assert not is_power_of_two(9)
    assert not is_power_of_two(-16)
