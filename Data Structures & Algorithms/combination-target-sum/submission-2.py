class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        path = []
        res = []

        def dfs(i, s):
            if i == len(nums) or s > target: 
                return 
            if s == target: 
                res.append(path.copy())
                return 
            
            
            path.append(nums[i])
            dfs(i, s + nums[i])

            path.pop()
            dfs(i + 1, s)
        
        dfs(0, 0)
        return res

