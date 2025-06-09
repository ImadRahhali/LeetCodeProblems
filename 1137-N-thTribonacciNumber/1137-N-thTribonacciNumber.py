# Last updated: 6/9/2025, 8:35:09 PM
class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0,1,1]

        if n < 3:
            return dp[n]
        i = 3
        while i <= n:
            tmp = dp[2]
            dp[2] = dp[0] + dp[1] + dp[2]
            dp[0] = dp[1]
            dp[1] = tmp
            i += 1
        return dp[2]
        
