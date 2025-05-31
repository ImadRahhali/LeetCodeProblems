# Last updated: 5/31/2025, 7:24:31 PM
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        def isSqrt(n):
            if n * n > x:
                return 1
            elif n * n < x:
                return -1
            else:
                return 0

        L, R = 1, x
        while L <= R:
            mid = (L + R) // 2
            if isSqrt(mid) > 0:
                R = mid - 1
            elif isSqrt(mid) < 0:
                L = mid + 1
            else:
                return mid

        return R
