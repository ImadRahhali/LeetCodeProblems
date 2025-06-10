# Last updated: 6/10/2025, 3:25:14 PM
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(n):
            if n == 0:
                return 0
            if n < 0:
                return -1
            if n in memo:
                return memo[n]

            min_coins = float('inf')
            
            for coin in coins:
                if dfs(n - coin) != -1:
                    min_coins = min(min_coins, 1 + dfs(n - coin))
        
            memo[n] = min_coins if min_coins != float('inf') else -1

            return memo[n]
        
        return dfs(amount)
        