# Last updated: 5/31/2025, 10:03:06 PM
class Solution:
    def findMin(self, nums: List[int]) -> int:
        L, R = 0, len(nums) -1
        while L < R:
            mid = (L+R)//2
            if nums[mid] > nums[R]:
                L = mid + 1
            elif nums[mid] < nums[R]:
                R = mid
            else:
                return nums[mid]
        return nums[L]

