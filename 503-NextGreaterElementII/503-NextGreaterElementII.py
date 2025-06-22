# Last updated: 6/22/2025, 10:01:30 AM
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        stack = [] # store indexes not values

        for i in range(2 * n):
            curr = nums[i % n]
            while stack and curr > nums[stack[-1]]:
                idx = stack.pop()
                res[idx] = curr
            if i < n:
                stack.append(i)
        return res
            
            