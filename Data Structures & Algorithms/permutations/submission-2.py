class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        path = []
        res = []
        def dfs(i): 
            if i == len(nums): 
                res.append(path.copy())
                return 
            
            for j in range(len(path) + 1):
                path.insert(j, nums[i])
                dfs(i + 1)
                path.pop(j)
        
        dfs(0)
        return res
