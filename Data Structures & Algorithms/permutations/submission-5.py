class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def backtrack(i): 
            nonlocal res 
            nonlocal path 
            if i == len(nums): 
                res.append(path.copy())
                return 
            
            for j in range(len(path) + 1): 
                path.insert(j, nums[i])
                backtrack(i + 1)
                path.pop(j)
            
        backtrack(0)
        return res