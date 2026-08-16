class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        dp = {}
        nums.insert(0, 1)
        nums.append(1)

        def dfs(l, r):
            # dp(l, r) = dp(l, k) + dp(k, r) + dp[k] * dp[l] * dp[r]
            if (l, r) in dp: 
                return dp[(l, r)]
            
            if l + 1 == r: 
                return 0
            
            res = 0
            for i in range(l + 1, r): 
                res = max(res, dfs(l, i) + dfs(i, r) + nums[i]*nums[l]*nums[r])
            
            dp[(l, r)] = res
            return res 
        
        
        return dfs(0, len(nums) - 1)