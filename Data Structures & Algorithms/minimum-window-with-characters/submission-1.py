class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dt = {}
        ds = {}

        for i in range(len(t)): 
            dt[t[i]] = dt.get(t[i], 0) + 1
        
        l = 0 
        count = 0
        lm = 0
        rm = float('inf')

        for r in range(len(s) + 1): 
            while count == len(dt): 
                if (rm - lm > r - l): 
                    lm = l 
                    rm = r
                if s[l] in dt: 
                    if ds[s[l]] == dt[s[l]]: 
                        count -= 1
                    ds[s[l]] -= 1
                l += 1
            
            if r < len(s) and s[r] in dt: 
                ds[s[r]] = ds.get(s[r], 0) + 1
                if ds[s[r]] == dt[s[r]]: 
                    count += 1
        

        if rm == float('inf'): 
            return ""
        else:
            return s[lm:rm]

