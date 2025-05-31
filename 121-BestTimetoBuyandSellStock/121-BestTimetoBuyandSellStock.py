# Last updated: 5/31/2025, 12:46:32 PM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        L = 0
        R = 1
        for R in range(1,len(prices)):
            if prices[R] < prices[L]:
                L = R
            else:
                max_profit = max(max_profit, prices[R] - prices[L])
        return max_profit
