# Last updated: 6/11/2025, 2:30:58 PM
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxheap = [[- math.sqrt(x*x + y*y) , [x,y]] for x,y in points[:k]]
        heapq.heapify(maxheap)
        for x,y in points[k:]:
            min_dist = - maxheap[0][0]
            dist = math.sqrt(x*x + y*y)
            if dist < min_dist:
                heapq.heappushpop(maxheap, [ - dist, [x,y]])
        return [maxheap[i][1] for i in range(len(maxheap))]
            