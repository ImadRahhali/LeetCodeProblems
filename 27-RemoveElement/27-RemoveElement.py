# Last updated: 5/30/2025, 7:35:12 PM
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        k = 0
        for i in range(n):
            if nums[i] != val:
                nums[k] = nums[i]
                k+=1 
        return k
        