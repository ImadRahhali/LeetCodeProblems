# Last updated: 5/30/2025, 7:34:16 PM
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = ""
        for i in range(min(len(word1),len(word2))):
            s += word1[i]
            s += word2[i]
        if len(word1) < len(word2):
            s += word2[len(word1):]
        elif len(word1) > len(word2):
            s += word1[len(word2):]
        return s
