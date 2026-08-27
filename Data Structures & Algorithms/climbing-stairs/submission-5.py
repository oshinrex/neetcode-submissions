class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * n
        # dp[i] = the number of possible ways you can reach that step 
        if n <= 2: 
            return n
        dp[0] = 1
        dp[1] = 2

        for i in range(2, n):
            dp[i] = dp[i - 2] + dp[i - 1]
        
        return dp[n - 1]
