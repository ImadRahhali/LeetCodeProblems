# Last updated: 6/16/2025, 2:42:49 PM
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        max_diff = -1
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    diff = nums[j] - nums[i]
                    max_diff = max(max_diff, diff)
        return max_diff