class Solution:
    def checkValidString(self, s: str) -> bool:
        dp = {}
        def dfs(diff, i):
            if i == len(s):
                if diff == 0: 
                    return True
                else:
                    return False
            
            if diff < 0: 
                return False
            
            if (diff, i) in dp:
                return dp[(diff, i)]

            if s[i] == "(":
                dp[(diff, i)] = dfs(diff + 1, i+1)
                
            elif s[i] == ")":
                dp[(diff, i)] = dfs(diff - 1, i+1)
                
            else:
                dp[(diff+1, i+1)] = dfs(diff+1, i+1)
                dp[(diff-1, i+1)] = dfs(diff-1, i+1)
                dp[(diff, i+1)] = dfs(diff, i+1)
                dp[(diff, i)] = dp[(diff+1, i+1)] or dp[(diff-1, i+1)] or dp[(diff, i+1)]
            return dp[(diff, i)]
        
        return dfs(0, 0)