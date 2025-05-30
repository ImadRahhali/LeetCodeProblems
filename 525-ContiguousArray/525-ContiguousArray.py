# Last updated: 5/30/2025, 7:34:32 PM
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        pre = {0: -1}
        currSum = 0
        max_length = 0
        for i in range(len(nums)):
            currSum += 1 if nums[i] == 1 else -1
            if currSum in pre:
                max_length = max(max_length, i - pre[currSum])
            else:
                pre[currSum] = i
        return max_length
