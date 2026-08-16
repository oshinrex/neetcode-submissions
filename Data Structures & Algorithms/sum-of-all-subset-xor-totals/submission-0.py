class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        def backtrack(i, s):
            nonlocal res
            if i == len(nums):
                res += s
                return 
            
            backtrack(i + 1, s ^ nums[i])
            backtrack(i + 1, s)
        
        backtrack(0, 0)
        return res 