# Last updated: 6/7/2025, 12:20:43 PM
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incoming = {i : 0 for i in range(1,n+1)}
        outcoming = {i : 0 for i in range(1,n+1)}

        for src, dist in trust:
            incoming[dist] += 1
            outcoming[src] += 1
        
        for i in range(1,n+1):
            if incoming[i] == n - 1 and outcoming[i] == 0:
                return i
        
        return -1
