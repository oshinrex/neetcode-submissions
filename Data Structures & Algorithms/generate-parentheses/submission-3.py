class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(o, c, paren): 
            if n == o == c: 
                res.append(paren)
                return 
            
            if o < n: 
                dfs(o + 1, c, paren + "(")
            if c < o: 
                dfs(o, c + 1, paren + ")")

        dfs(0, 0, "")          
        return res  