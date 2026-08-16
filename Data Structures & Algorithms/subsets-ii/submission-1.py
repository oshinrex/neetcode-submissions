class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        path = []
        res = []
        
        def dfs(i):
            if i == len(nums):
                res.append(path.copy())
                return 
            
            path.append(nums[i])
            dfs(i + 1)
            path.pop()
            
            j = i 
            while j < len(nums) and nums[i] == nums[j]:
                j += 1
            dfs(j)
            
        dfs(0)
        return res
