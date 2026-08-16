class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)

        dp[0] = nums[0]
        ret = dp[0]

        for i in range(1, len(nums)):
            max_cost = 0
            for j in range (i - 1):
                max_cost = max(max_cost, dp[j])
            dp[i] = nums[i] + max_cost
            ret = max(ret, dp[i])
    
        return ret


        