# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

from typing import List


class Solution:
    def max_profit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        max_profit = 0
        buy_idx = 0
        sell_idx = 1
        while sell_idx < len(prices):
            curr_profit = prices[sell_idx] - prices[buy_idx]
            max_profit = max(curr_profit, max_profit)
            if prices[buy_idx] > prices[sell_idx]:
                buy_idx = sell_idx
            sell_idx += 1
        return max_profit


print(Solution().max_profit(prices=[7, 1, 5, 3, 6, 4]))