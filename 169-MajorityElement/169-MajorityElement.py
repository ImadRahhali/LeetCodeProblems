# Last updated: 5/30/2025, 7:34:50 PM
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res , count = 0,0
        for num in nums:
            if count == 0:
                res = num
            count += (1 if num == res else -1)
        return res