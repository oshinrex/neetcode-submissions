class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        path = [] 
        res = []

        def dfs(n, total): 
            if total == target: 
                res.append(path.copy())
                return 


            for i in range(n, len(candidates)): 
                if i > n and candidates[i] == candidates[i-1]: 
                    continue 

                if total + candidates[i] > target:
                    break 
                
                path.append(candidates[i])
                dfs(i + 1, total + candidates[i])

                path.pop()
            
        dfs(0, 0)
        return res