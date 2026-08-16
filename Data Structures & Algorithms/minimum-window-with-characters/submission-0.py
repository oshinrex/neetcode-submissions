class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_hash = {}
        s_hash = {}

        l = r = 0
        l1 = r1 = 0

        max_sub = len(s) + 1

        for c in t:
            t_hash[c] = t_hash.get(c, 0) + 1

        matches = 0
        needed = len(t_hash)
        
        while r < len(s) or matches == needed:
            if matches == needed:
                if max_sub > r - l:
                    max_sub = r - l
                    l1 = l
                    r1 = r
                if s[l] in t_hash:
                    s_hash[s[l]] -= 1
                    if s_hash[s[l]] < t_hash[s[l]]:
                        matches -= 1
                l += 1
            else:
                if s[r] in t_hash:
                    s_hash[s[r]] = s_hash.get(s[r], 0) + 1
                    if s_hash[s[r]] == t_hash[s[r]]:
                        matches += 1
                r += 1

        if max_sub == len(s) + 1: 
            return "" 
        else: 
            return s[l1 : r1]