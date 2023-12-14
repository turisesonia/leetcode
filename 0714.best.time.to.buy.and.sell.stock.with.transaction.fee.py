"""
# 714
Medium
Best Time to Buy and Sell Stock with Transaction Fee

https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee

You are given an array prices where prices[i] is the price of a given stock on the ith day, and an integer fee representing a transaction fee.
Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.

Note:
* You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
* The transaction fee is only charged once for each stock purchase and sale.


Example 1:
Input: prices = [1,3,2,8,4,9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
- Buying at prices[0] = 1
- Selling at prices[3] = 8
- Buying at prices[4] = 4
- Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.

Example 2:
Input: prices = [1,3,7,5,10,3], fee = 3
Output: 6
- ((10 - 1) - 3) = 6

Constraints:
* 1 <= prices.length <= 5 * 104
* 1 <= prices[i] < 5 * 104
* 0 <= fee < 5 * 104

Hint:
Consider the first K stock prices. At the end, the only legal states are that you don't own a share of stock, or that you do.
Calculate the most profit you could have under each of these two cases.
"""


def max_profit(prices: list[int], fee: int) -> int:
    # 同一天無法買賣，所以第一天的 profit 為 0
    profit = 0

    # 預設第一天就買進股票, 所以一開始的持有資產為負數 (尚未賣掉, 一開始的持有資產為 -1 * prices[0])
    hold = -prices[0]

    for price in prices[1:]:
        # 先記錄前一日的收益
        prev_profit = profit

        # 計算若在第 i 日賣掉時可以拿到的最大收益
        profit = max(profit, price + hold - fee)

        # 在第 i 日時已經持有的資產 (這裡會有兩種狀況)
        # 1. 若前次交易的 profit 超過留到再隔一天賣掉的收益, 即第一個範例題目  (8-1)-2 + (9-4)-2 = 8, 在(8-1)-2時 計算出來的 hold 會大於前面持有的情況, 所以會發生多次交易
        # 2. 前次交易的 profit 不會超過留到在之後賣掉的收益
        hold = max(hold, prev_profit - price)

    # 因為是要找出最大收益, 最後一定要賣掉
    return profit


if __name__ == "__main__":
    assert max_profit(prices=[1, 3, 2, 8, 4, 9], fee=2) == 8
    assert max_profit(prices=[1, 3, 7, 5, 10, 3], fee=3) == 6
