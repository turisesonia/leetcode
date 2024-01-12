"""
# 122
Medium
Best Time to Buy and Sell Stock II

You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock.
You can only hold at most one share of the stock at any time.
However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.

Example 2:
Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.

Example 3:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.


Constraints:
* 1 <= prices.length <= 3 * 10^4
* 0 <= prices[i] <= 10^4
"""

from typing import List


def max_profit(prices: List[int]) -> int:
    # 假設第一天就買進股票, 所以一開始資產為 -1 * prices[0]
    hold = -prices[0]
    profit = 0

    for price in prices[1:]:
        prev_profit = profit

        # 計算在第 i 日時賣掉時可以拿到的最大收益
        profit = max(profit, hold + price)

        # 在第 i 日時已經持有資產 (這裡會有兩種狀況)
        # 1. 若前次交易的 profit 超過留到再隔一天賣掉的收益時, 計算出來的 hold 會大於前面持有的情況, 所以會發生多次交易
        # 2. 前次交易的 profit 不會超過留到在之後賣掉的收益
        hold = max(hold, prev_profit - price)

    return profit


if __name__ == "__main__":
    assert max_profit(prices=[7, 1, 5, 3, 6, 4]) == 7
    assert max_profit(prices=[1, 2, 3, 4, 5]) == 4
    assert max_profit(prices=[7, 6, 4, 3, 1]) == 0
