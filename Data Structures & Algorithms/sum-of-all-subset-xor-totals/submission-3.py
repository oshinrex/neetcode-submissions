class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        xor = 0
        def backtrack(i):
            nonlocal res 
            nonlocal xor

            if i == len(nums):
                res += xor
                return 
            
            prev = xor
            xor ^= nums[i]
            backtrack(i + 1)
            xor = prev 
            backtrack(i + 1)
        
        backtrack(0)
        return res