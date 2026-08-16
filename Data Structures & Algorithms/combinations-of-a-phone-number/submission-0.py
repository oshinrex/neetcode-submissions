class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        d_c = {2:"abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"}        
        res = []

        def dfs(i, num):
            if i == len(digits):
                res.append(num)
                return 
            
            for j in range(len(d_c[int(digits[i])])):
                dfs(i + 1, num + d_c[int(digits[i])][j])
        
        dfs(0, "")
        return res