class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        path = []
        res = []
        def backtrack(open, closed): 
            nonlocal path
            nonlocal res 
            if open == closed == n: 
                res.append("".join(path))
                return 
            
            if open > n or closed > n or closed > open: 
                return 
            
            path.append("(")
            backtrack(open + 1, closed)
            path.pop()
            path.append(")")
            backtrack(open, closed + 1)
            path.pop()
        
        backtrack(0, 0)
        return res
