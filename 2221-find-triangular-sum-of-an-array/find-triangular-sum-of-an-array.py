    def triangularSum(self, nums: List
[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        for i in range(len(nums)-1):
            newNums = [0] * (len(nums) - 
1)
            for j in range(len(newNums)):
                newNums[j] = (nums[j] + 
nums[j+1]) % 10
            nums = newNums
        return nums[0]