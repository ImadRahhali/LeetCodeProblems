# Last updated: 5/30/2025, 7:35:11 PM
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        n = len(nums)
        for i in range(1,n):
            if nums[k] != nums[i]:
                k+=1
                nums[k] = nums[i]
        return k+1
