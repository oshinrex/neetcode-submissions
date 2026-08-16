class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = {}
        def dfs(i, j):
            if (i, j) in dp: 
                return dp[(i, j)]
            
            if j == len(p): 
                return i == len(s)
            
            # first pattern
            if j+1 < len(p) and p[j+1] == "*": 
                dp[(i, j+2)] = dfs(i, j+2)
                if dp[(i, j+2)]:
                    return True 
                if i < len(s):
                    if p[j] == "." or p[j] == s[i]:
                        dp[(i+1, j)] = dfs(i+1, j)
                        if dp[(i+1, j)]:
                            return True

            # second pattern 
            if i < len(s) and (s[i] == p[j] or p[j] == "."):
                dp[(i + 1, j + 1)] = dfs(i+1, j+1)
                if dp[(i+1, j+1)]:
                    return True 
            

            return False
        
        return dfs(0, 0)