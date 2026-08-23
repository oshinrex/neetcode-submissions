class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        candidates.sort()

        def backtrack(i, curr_sum): 
            if curr_sum == target: 
                res.append(path.copy())
                return
            
            if curr_sum > target or i == len(candidates): 
                return 
            
            for j in range(i, len(candidates)): 
                if j > i and candidates[j] == candidates[j - 1]: 
                    continue 
                
                if candidates[j] + curr_sum > target: 
                    break
                
                path.append(candidates[j])
                backtrack(j + 1, curr_sum + candidates[j])
                path.pop()
        
        backtrack(0, 0)
        return res