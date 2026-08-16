class Solution:
    def jump(self, nums: List[int]) -> int:
        longest = float('inf')
        dp = [float('inf')] * len(nums)
        dp[len(nums) - 1] = 0

        for i in range(len(nums) - 2, -1, -1):
            for j in range(1,min(len(nums) - i, 1 + nums[i])):
                dp[i] = min(dp[i], dp[i+j])
            dp[i] += 1

        return int(dp[0])