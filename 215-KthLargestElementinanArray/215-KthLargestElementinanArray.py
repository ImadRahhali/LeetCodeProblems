# Last updated: 6/11/2025, 1:40:10 PM
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap = nums[:k]
        heapq.heapify(minheap)
        for num in nums[k:]:
            if num > minheap[0]:
                heapq.heappushpop(minheap, num)
        return minheap[0]