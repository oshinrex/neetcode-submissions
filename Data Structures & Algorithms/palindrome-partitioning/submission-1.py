class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []

        def backtrack(i): 
            nonlocal res
            nonlocal path 
            if i == len(s): 
                res.append(path.copy())
                return 
            
            for j in range(i, len(s)): 
                sub = s[i:j+1]
                if sub == sub[::-1]: 
                    path.append(sub)
                    backtrack(j+1)
                    path.pop()
        
        backtrack(0)
        return res