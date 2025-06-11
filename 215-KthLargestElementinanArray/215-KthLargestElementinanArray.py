# Last updated: 6/11/2025, 1:33:53 PM
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap = nums
        heapq.heapify(minheap)
        while len(minheap) > k:
            heapq.heappop(minheap)
        return minheap[0]