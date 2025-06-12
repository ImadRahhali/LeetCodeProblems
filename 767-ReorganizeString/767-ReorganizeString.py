# Last updated: 6/12/2025, 10:10:09 AM
class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        maxheap = [[-cnt, char] for char, cnt in counter.items()]
        heapq.heapify(maxheap)

        prev = None
        res = ""

        while maxheap or prev:
            if prev and not maxheap:
                return ""

            cnt, char = heapq.heappop(maxheap)
            res += char
            cnt +=1

            if prev:
                heapq.heappush(maxheap, prev)
                prev = None
            if cnt != 0:
                prev = [cnt, char]
        return res