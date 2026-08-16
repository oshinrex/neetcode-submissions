class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[len(nums) - 1] = 1
        res = 0
        
        for i in range(len(nums) - 2, -1, -1): 
            longest = 0
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    longest = max(longest, dp[j])
            dp[i] = longest + 1
        
        for n in dp: 
            res = max(n, res)
        
        return res