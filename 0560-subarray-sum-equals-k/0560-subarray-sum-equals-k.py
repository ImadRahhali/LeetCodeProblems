class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre = { 0 : 1}
        currSum = 0
        count = 0
        for num in nums:
            currSum += num
            diff = currSum - k

            count += pre.get(diff,0)
            pre[currSum] = 1 + pre.get(currSum,0)

        return count
