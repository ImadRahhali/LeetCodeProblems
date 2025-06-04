# Last updated: 6/4/2025, 5:29:18 PM
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * (n + 1)
        postfix = [1] * (n + 1)
        res = []
        prefix_p = 1
        postfix_p = 1
        for i in range(n):
            prefix_p *= nums[i]
            prefix[i+1] = prefix_p
        for i in range(n-1, -1, -1):
            postfix_p *= nums[i]
            postfix[i-1] = postfix_p
        for i in range(n):
            res.append(prefix[i] * postfix[i])
        
        return res
