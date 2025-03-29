
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix = strs[0]  # Start with the first word as the prefix
        
        for word in strs[1:]:  # Compare with remaining words
            i = 0
            while i < len(prefix) and i < len(word) and prefix[i] == word[i]:
                i += 1
            prefix = prefix[:i]  # Trim the prefix to the matching part
            
            if not prefix:  # If prefix becomes empty, return ""
                return ""
        
        return prefix
