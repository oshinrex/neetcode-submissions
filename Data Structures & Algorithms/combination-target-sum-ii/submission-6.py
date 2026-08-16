class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        path = []
        res = []
        
        def dfs(i, s): 
            if s == target: 
                res.append(path.copy())
                return 
            if i == len(candidates) or s > target: 
                return 

            curr = i 
            
            path.append(candidates[i])
            dfs(i + 1, s + candidates[i])
            while curr < len(candidates) and candidates[i] == candidates[curr]:
                curr += 1
            path.pop()
            dfs(curr, s)
        
        dfs(0, 0)
        return res
