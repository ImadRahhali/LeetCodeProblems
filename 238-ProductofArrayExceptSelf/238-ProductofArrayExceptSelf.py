# Last updated: 6/4/2025, 5:33:16 PM
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * (n + 1)
        postfix = [1] * (n + 1)
        res = [0] * n
        for i in range(n):
            prefix[i+1] = prefix[i] * nums[i]
        for i in range(n-1, -1, -1):
            postfix[i-1] = postfix[i] * nums[i]
        for i in range(n):
            res[i] = prefix[i] * postfix[i] 
        
        return res
