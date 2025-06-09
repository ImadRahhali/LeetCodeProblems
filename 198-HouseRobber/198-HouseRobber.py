# Last updated: 6/9/2025, 9:06:11 PM
class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}
        def dfs(i):
            if i >= len(nums):
                return 0
            if i in cache:
                return cache[i]
            cache[i] = max(nums[i] + dfs(i+2), dfs(i+1))
            return cache[i]
        
        return dfs(0)