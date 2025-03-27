class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sumDic = {} #val:index
        for i, n in enumerate(nums):
            diff = target - n
            if diff in sumDic:
                return [i, sumDic[diff]]
            sumDic[n] = i
        return
