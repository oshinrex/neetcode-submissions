class Solution:
    def integerBreak(self, n: int) -> int:
        # dp[i]: if you break i into pieces, its maximum product 

        dp = [1] * (n + 1)

        for i in range(2, n + 1):
            dp[i] = 0 if i == n else i
            for j in range(1, i):
                dp[i] = max(dp[i], dp[j] * dp[i - j])
        
        print(dp)
        return dp[n]
