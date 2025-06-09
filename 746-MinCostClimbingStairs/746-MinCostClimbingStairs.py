# Last updated: 6/9/2025, 8:14:12 PM
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        one, two = 0, 0
        for i in range(n-1, -1, -1):
            tmp = one
            one = cost[i] + min(one, two)
            two = tmp
        return min(one, two)