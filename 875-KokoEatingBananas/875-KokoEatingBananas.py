# Last updated: 5/31/2025, 9:06:04 PM
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L, R = 1, max(piles)
        res = R
        while L <= R:
            k = (L+R) // 2
            total = 0
            for p in piles:
                total += math.ceil(float(p)/k)
            if total <= h:
                res = k
                R = k -1
            else:
                L = k + 1
        return res