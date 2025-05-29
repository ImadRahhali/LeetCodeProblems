class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        currSum = 0
        remainder_freq = {0:1}
        count = 0
        for n in nums:
            currSum += n
            remainder = currSum % k

            if remainder < 0:
                remainder += k
            
            count += remainder_freq.get(remainder, 0)
            remainder_freq[remainder] = 1 + remainder_freq.get(remainder, 0)

        return count