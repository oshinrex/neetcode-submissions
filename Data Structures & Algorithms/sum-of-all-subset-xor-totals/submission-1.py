class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0 

        def backtrack(i, curr_sum):
            nonlocal res
            if i == len(nums):
                res += curr_sum
                return 
            
            backtrack(i + 1, curr_sum ^ nums[i])
            backtrack(i + 1, curr_sum)
        
        backtrack(0, 0)
        return res