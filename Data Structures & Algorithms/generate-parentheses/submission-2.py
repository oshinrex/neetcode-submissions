class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(o, c, paren): 
            if n == o == c: 
                res.append(paren)
                return 
            
            if o == n: 
                paren = paren + ")"
                dfs(o, c + 1, paren)
            elif c < o: 
                temp = paren
                paren = paren + "("
                dfs(o + 1, c, paren)

                paren = temp 
                paren = paren + ")"
                dfs(o, c + 1, paren)
            else: 
                paren = paren + "("
                dfs(o + 1, c, paren)

        dfs(0, 0, "")          
        return res  