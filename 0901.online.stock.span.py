"""
# 901
Medium
Online Stock Span

https://leetcode.com/problems/online-stock-span

Design an algorithm that collects daily price quotes for some stock and returns the span of that stock's price for the current day.
The span of the stock's price in one day is the maximum number of consecutive days (starting from that day and going backward) for which the stock price was less than or equal to the price of that day.

For example, if the prices of the stock in the last four days is [7,2,1,2] and the price of the stock today is 2, then the span of today is 4 because starting from today, the price of the stock was less than or equal 2 for 4 consecutive days.

Also, if the prices of the stock in the last four days is [7,34,1,2] and the price of the stock today is 8, then the span of today is 3 because starting from today, the price of the stock was less than or equal 8 for 3 consecutive days.

Implement the StockSpanner class:
StockSpanner() Initializes the object of the class.
int next(int price) Returns the span of the stock's price given that today's price is price.

Example 1:
Input
["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
[[], [100], [80], [60], [70], [60], [75], [85]]
Output
[null, 1, 1, 1, 2, 1, 4, 6]

Explanation
StockSpanner stockSpanner = new StockSpanner();
stockSpanner.next(100); // return 1
stockSpanner.next(80);  // return 1
stockSpanner.next(60);  // return 1
stockSpanner.next(70);  // return 2
stockSpanner.next(60);  // return 1
stockSpanner.next(75);  // return 4, because the last 4 prices (including today's price of 75) were less than or equal to today's price.
stockSpanner.next(85);  // return 6

Constraints:
1 <= price <= 105
At most 104 calls will be made to next.
"""


class StockSpanner:
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        # ! Time Limit Exceeded
        """
        Broute-force solution

        check price in stack every time have new price arrivel
        """
        span = 1

        for num in self.stack:
            if num > price:
                break
            else:
                span += 1

        self.stack.insert(0, price)

        return span

    def next(self, price: int) -> int:
        """
        本題要找的答案其實就是新的價格進來後，將前面所有 "小於等於" 此價格的數量回傳。

        1. 利用 stack 記錄每個股票的 "價格" 以及 "連續跨度天數" (price, days), days 至少等於 1
        2. 當 stack 內沒有價格記錄時，直接將當下的 (價格, 1) 存入 stack
        3. 接下來一直做以下檢查，直到 stack[-1] 的 price > current price
           3.1 如果 stack[-1][0] (price) 小於等於 new price
           3.2 取出 (pop) 最後這個 (price, days), 將 temp days += days
        4. 最後再將 (current price, temp days) 存入 stack 內
        """
        days = 1

        while self.stack and self.stack[-1][0] <= price:
            n = self.stack.pop()
            days += n[1]

        self.stack.append((price, days))

        return days


if __name__ == "__main__":
    # Your StockSpanner object will be instantiated and called as such:
    spanner = StockSpanner()
    assert spanner.next(100) == 1
    assert spanner.next(80) == 1
    assert spanner.next(60) == 1
    assert spanner.next(70) == 2
    assert spanner.next(60) == 1
    assert spanner.next(75) == 4
    assert spanner.next(85) == 6
