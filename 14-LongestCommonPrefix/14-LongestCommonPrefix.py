# Last updated: 5/30/2025, 7:35:27 PM
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:          
        pre = ""
        for i in range(len(strs[0])):
            for word in strs:
                if i == len(word) or word[i]!=strs[0][i]:
                    return pre
            pre += strs[0][i]
        return pre
