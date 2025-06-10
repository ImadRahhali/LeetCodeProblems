# Last updated: 6/10/2025, 10:11:54 AM
class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_substring = ""
        length = 0
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l +1) > length:
                    length = r - l +1
                    max_substring = s[l: r+1]
                l -= 1
                r += 1
            l, r = i, i+1
            while l >= 0 and r< len(s) and s[l] == s[r]:
                if (r - l +1) > length:
                    length = r - l +1
                    max_substring = s[l: r+1]
                l -= 1
                r += 1
        return max_substring