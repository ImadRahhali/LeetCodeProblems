# Last updated: 6/11/2025, 1:57:26 PM
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = [-x for x in stones]
        heapq.heapify(maxheap)
        while len(maxheap) > 1:
            first = - heapq.heappop(maxheap)
            second = - heapq.heappop(maxheap)
            if first != second:
                heapq.heappush(maxheap, - (first - second))
        return - maxheap[0] if len(maxheap) == 1 else 0


            
