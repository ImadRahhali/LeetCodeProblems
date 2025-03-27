class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sumDic = {}
        for i in range(len(nums)):
            if target - nums[i] in sumDic:
                return [i, sumDic[target - nums[i]]]
            sumDic[nums[i]] = i
        return []
