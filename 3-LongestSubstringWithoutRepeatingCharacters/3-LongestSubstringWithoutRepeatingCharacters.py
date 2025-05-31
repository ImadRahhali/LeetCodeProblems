# Last updated: 5/31/2025, 1:08:00 PM
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        max_length = 0
        L = 0
        R = 0
        while R < len(s):
            if s[R] in window:
                window.remove(s[L])
                L += 1
            else:
                window.add(s[R])
                R += 1
            max_length = max(max_length, R - L)
        return max_length