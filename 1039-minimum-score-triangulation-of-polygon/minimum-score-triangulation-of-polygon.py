class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        @lru_cache(None)
        def dp(i, j):
            if j - i < 2: return 0

            res = float('inf')

            for k in range(i+1, j):
                curr = values[i] * values[j] * values[k]
                res = min(res, curr + dp(i, k) + dp(k, j))
            
            return res