class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp[i] the maximum amount the robber can rob until the ith house if the ith house is included 
        if not nums: 
            return 0 

        if len(nums) <= 2: 
            return max(nums)
        
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = nums[1]

        if len(nums) > 2: 
            dp[2] = nums[2] + nums[0]
 
        for i in range(3, len(nums)): 
            dp[i] = nums[i] + max(dp[i - 2], dp[i - 3])
        
        return max(dp[-1], dp[-2])