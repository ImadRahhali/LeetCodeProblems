# Last updated: 5/31/2025, 11:56:57 AM
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = float('inf')
        L = 0
        total = 0

        for R in range(len(nums)):
            total += nums[R]
            while total >= target:
                min_length = min(min_length, R - L + 1)
                total -= nums[L]
                L += 1
        return 0 if min_length == float('inf') else min_length