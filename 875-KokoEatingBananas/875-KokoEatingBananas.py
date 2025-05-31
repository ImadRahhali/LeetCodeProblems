# Last updated: 5/31/2025, 8:34:35 PM
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def isCorrect(k):
            return sum((x + k - 1) // k for x in piles) <= h

        max_bananas = max(piles)
        L = 1
        R = max_bananas

        k = R

        while L <= R:
            mid = (L + R) // 2
            if isCorrect(mid):
                k = mid
                R = mid - 1
            else:
                L = mid + 1

        return k
