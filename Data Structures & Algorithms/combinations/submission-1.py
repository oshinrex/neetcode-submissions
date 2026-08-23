class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        path = []
        res = []

        def backtrack(ind, j): 
            nonlocal path
            nonlocal res 
            if j == k: 
                res.append(path.copy())
                return 
            
            if ind == n + 1: 
                return 
            
            backtrack(ind + 1, j)
            path.append(ind)
            backtrack(ind + 1, j + 1)
            path.pop()
        
        backtrack(1, 0)
        return res