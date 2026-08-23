class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        
        def backtrack(xor, i): 
            nonlocal res
            if i == len(nums): 
                res += xor
                return 
            
            backtrack(xor, i + 1)
            backtrack(xor ^ nums[i], i + 1)
        
        backtrack(0, 0)
        return res