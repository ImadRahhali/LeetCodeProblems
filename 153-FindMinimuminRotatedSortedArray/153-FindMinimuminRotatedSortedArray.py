# Last updated: 5/31/2025, 10:12:11 PM
class Solution:
    def findMin(self, nums: List[int]) -> int:
        L, R = 0, len(nums) -1
        res = nums[0]

        while L <= R:
            if nums[L] < nums[R]:
                return min(res, nums[L])
                break
            mid = (L+R) // 2
            res = min(res, nums[mid])

            if nums[mid] >= nums[L]:
                L = mid + 1
            else:
                R = mid - 1
        return res

