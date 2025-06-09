# Last updated: 6/9/2025, 8:29:51 PM
class Solution:
    def tribonacci(self, n: int) -> int:
        cache = {}
        def memo(n):
            if n <= 1:
                return n
            if n == 2:
                return 1

            if n in cache:
                return cache[n]
        
            cache[n] = memo(n-1) + memo(n-2) + memo(n-3)
            return cache[n]
        
        return memo(n)
