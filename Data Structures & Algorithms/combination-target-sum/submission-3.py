class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def backtrack(i, s):
            if s == target:
                res.append(path.copy())
                return 
            
            if s > target or i == len(nums):
                return 
            
            path.append(nums[i])
            backtrack(i, s + nums[i])
            path.pop()
            backtrack(i + 1, s)

            
        backtrack(0, 0)
        return res