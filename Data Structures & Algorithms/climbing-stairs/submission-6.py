class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n)
        for i in range(n): 
            if i <= 1: 
                dp[i] = i + 1
                continue
            
            dp[i] = dp[i - 1] + dp[i - 2]
        
        print(dp)
        return dp[-1]
            

