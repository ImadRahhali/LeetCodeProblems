# Last updated: 6/9/2025, 4:00:40 PM
class Solution:
    def fib(self, n: int) -> int:
        cache = {}
        def memo(n):
            if n <= 1:
                return n
            
            if n in cache:
                return cache[n]
            
            cache[n] = memo(n-1) + memo(n-2)
            return cache[n]
        
        return memo(n)
        