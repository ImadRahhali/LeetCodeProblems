class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sumDic = {}
        for i in nums:
            sumDic[i] = target - i
        
        for i in range(len(nums)):
            if sumDic[nums[i]] in nums and nums.index(sumDic[nums[i]]) != i:
                return [nums.index(sumDic[nums[i]]), i]
        return []
