# Last updated: 5/30/2025, 7:35:00 PM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0
        profit = 0
        for R in range(len(prices)):
            if prices[L] > prices[R]:
                L = R
            profit = max(profit, prices[R] - prices[L])
        return profit