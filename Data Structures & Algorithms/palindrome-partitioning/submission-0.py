class Solution:
    def partition(self, s: str) -> List[List[str]]:
        path = []
        res = []

        def palidrome(word):
            s, e = 0, len(word) - 1

            while s < e: 
                if word[s] != word[e]:
                    return False
                s += 1
                e -= 1
    
            return True 

        def dfs(i): 
            if i == len(s): 
                res.append(path.copy())
                return 
            
            for j in range(i, len(s)):
                if palidrome(s[i:j+1]):
                    path.append(s[i:j+1])
                    dfs(j+1)
                    path.pop()
            
            return
        
        dfs(0)
        return res