class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res , count = 0,0
        for num in nums:
            if count == 0:
                res = num
                count += 1
            count += (1 if num == res else -1)
            
            print(res)
            print(count)
        return res