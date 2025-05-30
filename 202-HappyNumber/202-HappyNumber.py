# Last updated: 5/30/2025, 7:34:47 PM
class Solution:
    def isHappy(self, n: int) -> bool:
        '''return True'''
        s = set()
        while n!=1:
            if n in s:
                return False
            s.add(n)
            n = sum(int(c) ** 2 for c in str(n))
        return True
