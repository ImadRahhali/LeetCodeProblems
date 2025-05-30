# Last updated: 5/30/2025, 7:34:35 PM
class NumArray:

    def __init__(self, nums: List[int]):
        total = 0
        self.prefix_sums = []
        for n in nums:
            total += n
            self.prefix_sums.append(total)

    def sumRange(self, left: int, right: int) -> int:
        left_sum = self.prefix_sums[left-1] if left > 0 else 0
        right_sum = self.prefix_sums[right]
        return right_sum - left_sum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)