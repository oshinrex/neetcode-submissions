class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # prices[i]: price of neetcoin on ith day 
        dp = {}

        def dfs(i, buying): 
            if i >= len(prices):
                return 0 
            
            if (i, buying) in dp: 
                return dp[(i, buying)]
            
            if buying:
                buy = -1 * prices[i] + dfs(i + 1, not buying)
                cooldown = dfs(i + 1, buying)
                dp[(i, buying)] = max(buy, cooldown)
            else: 
               sell = dfs(i + 2, not buying) + prices[i]
               cooldown = dfs(i + 1, buying)
               dp[(i, buying)] = max(sell, cooldown)
            
            return dp[(i, buying)]
        
        return dfs(0, True)