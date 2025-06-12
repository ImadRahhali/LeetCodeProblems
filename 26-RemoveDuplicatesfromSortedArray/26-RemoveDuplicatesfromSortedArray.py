# Last updated: 6/12/2025, 6:09:57 AM
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        n = len(nums)
        for i in range(1,n):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k+=1
        return k
