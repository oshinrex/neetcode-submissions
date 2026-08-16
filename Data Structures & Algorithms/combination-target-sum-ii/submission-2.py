class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        path = []
        res = []

        def dfs(sum, i): 
            if sum == target: 
                res.append(path.copy())
                return 
            if sum > target or i == len(candidates): 
                return 
            
            path.append(candidates[i])
            if sum + candidates[i] <= target:
                dfs(sum + candidates[i], i + 1)

            path.pop() 
            n = i 
            while i < len(candidates) and candidates[i] == candidates[n]:
                i += 1
            dfs(sum, i)
        dfs(0, 0)
        return res

