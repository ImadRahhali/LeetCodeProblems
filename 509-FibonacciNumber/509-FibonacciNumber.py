# Last updated: 6/9/2025, 4:09:05 PM
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        dp = [0,1]
        i = 2
        while i <= n:
            tmp = dp[1]
            dp[1] = dp[1] + dp[0]
            dp[0] = tmp
            i += 1
        return dp[1]
        