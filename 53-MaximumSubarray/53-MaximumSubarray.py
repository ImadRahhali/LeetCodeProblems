# Last updated: 5/30/2025, 7:35:07 PM
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currSum = 0
        for n in nums:
            if currSum < 0:
                currSum = 0
            currSum+=n
            maxSum = max(maxSum, currSum)
        return maxSum