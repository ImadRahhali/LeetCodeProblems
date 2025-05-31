# Last updated: 5/31/2025, 2:00:57 PM
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0
        L = 0
        mp = {}
        max_freq = 0
        for R in range(len(s)):
            mp[s[R]] = 1 + mp.get(s[R], 0)
            max_freq = max(max_freq, mp[s[R]])
            if (R - L + 1) - max_freq > k:
                mp[s[L]] -= 1
                L += 1
            max_length = max(max_length, R - L + 1)
        return max_length
