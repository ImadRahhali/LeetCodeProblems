# Last updated: 6/1/2025, 12:39:34 PM
class Solution:
    def findMin(self, nums: List[int]) -> int:
        L, R = 0, len(nums) - 1
        res = nums[0]

        while L <= R:
            mid = (L + R) // 2
            res = min(res, nums[mid])

            if nums[mid] > nums[R]:
                L = mid + 1
            else:
                R = mid - 1

        return res
