class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        path = []
        res = []

        def backtrack(i, length):
            nonlocal path 
            nonlocal res
            if length == k:
                res.append(path.copy())
                return 
            
            if i > n:
                return 
            
            path.append(i)
            backtrack(i + 1, length + 1)
            path.pop()
            backtrack(i + 1, length)
        
        backtrack(1, 0)
        return res
