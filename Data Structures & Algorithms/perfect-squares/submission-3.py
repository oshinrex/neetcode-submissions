class Solution:
    def numSquares(self, n: int) -> int:
        # minimum number of squares to ith term 
        dp = [n] * (n + 1)
        dp[0] = 0
        dp[1] = 1


        for i in range(2, len(dp)):
            for j in range(int(n ** 0.5) + 2):
                if i - j * j >= 0:
                    dp[i] = min(dp[i], dp[i - j*j] + 1)
                else:
                    break

        return dp[n]
