# Last updated: 6/9/2025, 8:33:35 PM
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1

        dp = [0,1,1]
        i = 3
        while i <= n:
            tmp = dp[2]
            dp[2] = dp[0] + dp[1] + dp[2]
            dp[0] = dp[1]
            dp[1] = tmp
            i += 1
        return dp[2]
        
