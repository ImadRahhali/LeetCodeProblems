class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr = [0]*26
        for char in s:
            arr[ord(char)-ord('a')]+=1
        for char in t:
            arr[ord(char)-ord('a')]-=1
        for val in arr:
            if val != 0:
                return False
        return True

