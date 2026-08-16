class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs or len(strs[0]) == 0: 
            return ""

        res = ""
        curr = 0
        c = strs[0][0]

        while True:
            for i in range(len(strs)):
                if curr >= len(strs[i]) or strs[i][curr] != c:
                    return res 
            
            res += c
            curr += 1

            if curr >= len(strs[0]):
                break 
            c = strs[0][curr]
        
        return res