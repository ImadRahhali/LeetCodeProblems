class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter={}
        for i in range(len(nums)):
            if nums[i] in counter:
                counter[nums[i]] += 1
            else:
                counter[nums[i]] = 1
        for num in counter:
            if counter[num] > len(nums)/2:
                return num