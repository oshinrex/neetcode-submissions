class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        fst = strs[0]

        prefix = ""

        for j in range(len(fst)): 
            for i in range(1, len(strs)):
                word = strs[i]
                if j == len(word) or word[j] != fst[j]:
                    return prefix 
            prefix += fst[j]
        
        return prefix