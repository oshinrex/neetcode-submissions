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
            
            if open < n: 
                path.append("(")
                backtrack(open + 1, closed)
                path.pop()
            
            if closed < open:
                path.append(")")
                backtrack(open, closed + 1)
                path.pop()
        
        backtrack(0, 0)
        return res
