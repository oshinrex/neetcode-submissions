class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3: 
            return max(nums)

        dp = [0] * (len(nums) - 1)
        dp2 = [0] * (len(nums) - 1)

        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        dp2[0], dp2[1] = nums[1], max(nums[1], nums[2])

        for i in range(2, len(nums) - 1): 
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
        
        for i in range(3, len(nums)):
            dp2[i - 1] = max(dp2[i - 2], nums[i] + dp2[i - 3])

        return max(dp[-1], dp2[-1])