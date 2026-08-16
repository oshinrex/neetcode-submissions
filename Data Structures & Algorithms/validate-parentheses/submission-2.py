class Solution:
    def isValid(self, s: str) -> bool:
        pair = {"]" : "[", ")" : "(", "}" : "{"}
        q = []

        for c in s: 
            if c in pair: 
                if q and q[-1] == pair[c]:
                    q.pop(-1)
                else:
                    return False
            else: 
                q.append(c)
        
        if q: 
            return False
        else: 
            return True
