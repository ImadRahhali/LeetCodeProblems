class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        k = n
        for i in range(n):
            if nums[i] == val:
                nums[i] = -1
                k -=1
        nums.sort()
        nums.reverse()
        return k
        