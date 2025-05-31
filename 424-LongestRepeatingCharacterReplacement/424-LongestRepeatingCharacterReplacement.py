# Last updated: 5/31/2025, 1:59:04 PM
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0
        L = 0
        mp = {}
        for R in range(len(s)):
            mp[s[R]] = 1 + mp.get(s[R], 0)
            diff_chars = (R-L+1) - max(mp.values())
            if diff_chars > k:
                mp[s[L]] -= 1
                L += 1
            max_length = max(max_length, R - L + 1)
        return max_length
