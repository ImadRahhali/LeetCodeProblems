# Last updated: 5/30/2025, 7:34:39 PM
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr = [0]*26
        for c in s:
            arr[ord(c)-ord('a')] += 1
        for c in t:
            arr[ord(c)-ord('a')] -= 1

        for i in arr:
            if i != 0:
                return False
        return True


