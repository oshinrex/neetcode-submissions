class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        longest = nums[0]
        prefix = longest

        for i in range(1, len(nums)):
            longest = max(longest, prefix)
            if prefix < 0:
                prefix = nums[i]
            else: 
                prefix += nums[i]
            
        return max(longest, prefix)