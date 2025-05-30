# Last updated: 5/30/2025, 8:00:17 PM
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_avg =  float('-inf')
        L = 0
        s = 0
        for R in range(len(nums)):
            s += nums[R]
            if R - L + 1 > k:
                s -= nums[L]
                L += 1
            if R - L == k -1:
                max_avg = max(max_avg, s/k)

        return max_avg