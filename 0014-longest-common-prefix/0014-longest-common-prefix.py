class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix = strs[0]
        
        for word in strs[1:]:
            while not word.startswith(prefix):
                prefix = prefix[:-1]  # Reduce prefix character by character
                if not prefix:
                    return ""
        
        return prefix

