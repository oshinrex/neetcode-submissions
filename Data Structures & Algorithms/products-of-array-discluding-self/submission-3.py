class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        suffix = 1

        for r in range(len(res) - 1, -1, -1):
            res[r] = suffix
            suffix *= nums[r]
        
        prefix = 1
        for l in range(len(res)):
            res[l] *= prefix
            prefix *= nums[l]
    
        return res