class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anag = {}
        res = []
        for word in strs:
            sWord = str(sorted(word))
            if sWord in anag:
                anag[sWord].append(word)
            else:
                anag[sWord] = [word]
        for lis in anag.values():
            res.append(lis)
        return res