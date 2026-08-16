class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # find all products to left 
        left = [1] * len(nums)
        for i in range(1, len(nums)):
            left[i] = nums[i - 1] * left[i - 1]
        print(left)

        # find all products to right
        right = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            right[i] = nums[i + 1] * right[i + 1]
        print(right)

        # find final output 
        res = [0] * len(nums)
        for i in range(len(nums)):
            res[i] = right[i] * left[i]
        
        return res
