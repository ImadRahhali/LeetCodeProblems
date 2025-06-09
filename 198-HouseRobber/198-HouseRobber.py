# Last updated: 6/9/2025, 9:20:19 PM
class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for n in nums:
            tmp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = tmp
        return rob2
        
        
        
        '''cache = {}
        def dfs(i):
            if i >= len(nums):
                return 0
            if i in cache:
                return cache[i]
            cache[i] = max(nums[i] + dfs(i+2), dfs(i+1))
            return cache[i]
        
        return dfs(0)'''