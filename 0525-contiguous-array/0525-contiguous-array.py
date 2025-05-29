class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        pre = {0:0}
        currSum = 0
        max_length = 0
        for i in range (len(nums)):
            length = 0
            currSum += 1 if nums[i] == 1 else -1
            if currSum in pre:
                length = i+1 - pre[currSum]
            else:
                pre[currSum] = i+1
            max_length = max(max_length, length)
            
        return max_length


            
        
