class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = -1
        
        currSum = 0
        pre = {0:0}
        max_length = 0
        for i in range (len(nums)):
            length = 0
            currSum += nums[i]
            if currSum in pre:
                length = i+1 - pre[currSum]
            else:
                pre[currSum] = i+1
            max_length = max(max_length, length)
            
        return max_length

#{0:0, -1:1,}

            
        
