class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s1 = {}
        t1 = {}

        for i in range(len(s)):
            s1[s[i]] = s1.get(s[i], 0) + 1
            t1[t[i]] = t1.get(t[i], 0) + 1
        
        for c in s1.keys(): 
            if c not in t1 or s1[c] != t1[c]:
                return False
        
        return True