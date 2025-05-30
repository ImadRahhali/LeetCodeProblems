# Last updated: 5/30/2025, 7:34:18 PM
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        min_dist = abs(nums[0])
        closest = nums[0]
        for num in nums[1:]:
            dist = abs(num)
            if dist < min_dist:
                min_dist = dist
                closest = num
            elif dist == min_dist:
                closest = max(closest,num)
        return closest
