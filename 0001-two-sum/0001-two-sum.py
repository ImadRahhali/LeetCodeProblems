class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sumDic = {}
        for i in range(len(nums)):
            sumDic[nums[i]] = i
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in sumDic and i != sumDic[diff]:
                return [i, sumDic[diff]] 