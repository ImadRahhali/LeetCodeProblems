# Last updated: 5/31/2025, 9:08:10 PM
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L, R = 1, max(piles)
        res = R
        while L <= R:
            k = (L+R) // 2
            total_hours = 0
            for p in piles:
                total_hours += math.ceil(p/k)
            if total_hours <= h:
                res = k
                R = k -1
            else:
                L = k + 1
        return res