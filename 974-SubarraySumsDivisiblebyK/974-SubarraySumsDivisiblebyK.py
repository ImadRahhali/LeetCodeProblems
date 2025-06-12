# Last updated: 6/12/2025, 6:26:24 AM
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        currSum = 0
        remainder_freq = {0:1}
        count = 0
        for n in nums:
            currSum += n
            remainder = currSum % k
            
            count += remainder_freq.get(remainder, 0)
            remainder_freq[remainder] = 1 + remainder_freq.get(remainder, 0)

        return count