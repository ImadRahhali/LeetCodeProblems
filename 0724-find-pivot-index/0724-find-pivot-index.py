class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = 0
        prefix_sums = [0]
        for n in nums:
            total += n
            prefix_sums.append(total)
        
        for i in range(len(nums)):
            left_sum = prefix_sums[i]
            right_sum = prefix_sums[len(nums)] - prefix_sums[i+1]
            print(prefix_sums)
            if right_sum == left_sum:
                return i
        return -1
