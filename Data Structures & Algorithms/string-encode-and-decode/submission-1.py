class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs: 
            res += str(len(s)) + "#" + s
        
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            str_len = ""
            # first find len of str
            while s[i] != "#":
                str_len += s[i]
                i += 1
            str_len = int(str_len)
            i += 1

            word = ""
            # find word
            while str_len > 0:
                word += s[i]
                i += 1
                str_len -= 1
            
            # append word to res 
            res.append(word)
        
        return res

