"""
Medium
# 2336
Smallest Number in Infinite Set

https://leetcode.com/problems/smallest-number-in-infinite-set

You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].

Implement the SmallestInfiniteSet class:
SmallestInfiniteSet() Initializes the SmallestInfiniteSet object to contain all positive integers.
int popSmallest() Removes and returns the smallest integer contained in the infinite set.
void addBack(int num) Adds a positive integer num back into the infinite set, if it is not already in the infinite set.

Example 1:
Input
["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest", "popSmallest", "addBack", "popSmallest", "popSmallest", "popSmallest"]
[[], [2], [], [], [], [1], [], [], []]
Output
[null, null, 1, 2, 3, null, 1, 4, 5]

Explanation
SmallestInfiniteSet smallestInfiniteSet = new SmallestInfiniteSet();
smallestInfiniteSet.addBack(2);    // 2 is already in the set, so no change is made.
smallestInfiniteSet.popSmallest(); // return 1, since 1 is the smallest number, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 2, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 3, and remove it from the set.
smallestInfiniteSet.addBack(1);    // 1 is added back to the set.
smallestInfiniteSet.popSmallest(); // return 1, since 1 was added back to the set and
                                   // is the smallest number, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 4, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 5, and remove it from the set.


Constraints:

1 <= num <= 1000
At most 1000 calls will be made in total to popSmallest and addBack.
"""


class SmallestInfiniteSet:
    """
    利用 min heap 解, 因題目限制只會呼叫 1000 次, 所以一開始就將 1~1000 設定進 heap
    速度較慢
    """

    def __init__(self):
        self.heap = [None]
        self.length = 0

        for i in range(1, 1001):
            self.addBack(i)

    def popSmallest(self) -> int:
        if self.length == 0:
            return None

        self._exchange(1, -1)
        min_ = self.heap.pop()
        self.length -= 1

        self._down_check()

        return min_

    def addBack(self, num: int) -> None:
        if num not in self.heap:
            self.heap.append(num)
            self.length += 1

            self._up_check(self.length)

    def _up_check(self, idx: int):
        while idx > 1 and self.heap[idx] < self.heap[idx // 2]:
            self._exchange(idx, idx // 2)
            idx //= 2

    def _down_check(self):
        idx = 1

        while idx <= self.length // 2:
            num = self.heap[idx]

            k = 2 * idx
            if k + 1 <= self.length and self.heap[k + 1] < self.heap[k]:
                k = k + 1

            if num < self.heap[k]:
                break
            else:
                self._exchange(idx, k)
                idx = k

    def _exchange(self, i: int, j: int):
        tmp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = tmp


class SmallestInfiniteSet:
    """
    Handle a infinite integers set
    1. Variable current 用來記錄上一次取出的最小數字是多少
    2. Variable set_ 記錄當執行 addBack 時, 如果數值小於等於 current, 則將此數字紀錄至 set_,
    3. popSmallest 時檢查兩個步驟
       3.1 set_ 內是否有數值, 有的話將其最小值取出並回傳
       3.2 若 set_ 為空, 則將 current += 1 並回傳
    """

    def __init__(self):
        self.set_ = set()
        self.current = 0

    def popSmallest(self) -> int:
        if len(self.set_) > 0:
            min_ = min(self.set_)
            self.set_.remove(min_)
            return min_

        self.current += 1

        return self.current

    def addBack(self, num: int) -> None:
        if num <= self.current:
            self.set_.add(num)


if __name__ == "__main__":
    inf_set = SmallestInfiniteSet()

    for num in [6, 5, 4, 1, 10, 7, 3, 9]:
        inf_set.addBack(num)

    assert inf_set.popSmallest() == 1
    assert inf_set.popSmallest() == 2
    inf_set.addBack(1)
    assert inf_set.popSmallest() == 1
    inf_set.addBack(2)

    assert inf_set.popSmallest() == 2
