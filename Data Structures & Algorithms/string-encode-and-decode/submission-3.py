class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs: 
            res += ("#" + str(len(s)) + " " + s)
        
        return res

    def decode(self, s: str) -> List[str]:
        if len(s) == 0: 
            return []
        
        res = []
        i = 0 

        while i < len(s): 
            num = s[i + 1: s.find(" ", i)]
            num = int(num)
            
            word = ""
            res.append(s[i + len(str(num)) + 2 : i + len(str(num)) + num + 2])
            i = i + len(str(num)) + num + 2
        
        return res