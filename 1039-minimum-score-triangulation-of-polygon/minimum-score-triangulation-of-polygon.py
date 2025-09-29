            if j - i < 2: return 0

            res = float('inf')

            for k in range(i+1, j):
        def dp(i, j):
                curr = values[i] * values[j] * values[k]
                res = min(res, curr + dp(i, k) + dp(k, j))
            
·‌·‌·‌·‌·‌·‌·‌·‌@cache
    def minScoreTriangulation(self, values: List[int]) -> int:
class Solution:
            return res