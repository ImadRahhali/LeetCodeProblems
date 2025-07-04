# Last updated: 6/9/2025, 4:46:32 PM
class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        for i in range(n-1):
            tmp = one
            one = one + two
            two = tmp
        return one
