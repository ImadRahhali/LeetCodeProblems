# Last updated: 6/15/2025, 10:40:09 PM
class Solution:
    def maxDiff(self, num: int) -> int:
        num = str(num)
        a = num
        for x in num:
            if x != '9':
                a = num.replace(x, '9')
                break
        
        b = num
        for x in num:
            if x == num[0] and x!='1':
                b = num.replace(x, '1')
                break
            if x != num[0] and x != '0':
                b = num.replace(x, '0')
                break
        
        return int(a) - int(b)
        