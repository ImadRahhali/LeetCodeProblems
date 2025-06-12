# Last updated: 6/12/2025, 5:57:25 AM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sumDic = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in sumDic:
                return [i, sumDic[diff]]
            sumDic[nums[i]] = i
        return []
