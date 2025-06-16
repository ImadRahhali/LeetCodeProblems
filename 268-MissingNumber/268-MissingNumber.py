# Last updated: 6/16/2025, 2:41:01 PM
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = sum(nums)
        n = len(nums)

        realSum = int((n*(n+1))/2)
        return realSum - s