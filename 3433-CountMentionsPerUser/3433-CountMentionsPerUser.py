# Last updated: 6/17/2025, 8:29:18 PM
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        max_freq = 0
        initial_count = nums.count(k)
        for target in set(nums):
            if target == k:
                continue
            
            curr_gain, max_gain = 0, 0
            for num in nums:
                if num == target:
                    curr_gain += 1
                elif num == k:
                    curr_gain -= 1
                
                max_gain = max(max_gain, curr_gain)
                curr_gain = max(curr_gain, 0)

            max_freq = max(max_freq, max_gain)
        return initial_count + max_freq
