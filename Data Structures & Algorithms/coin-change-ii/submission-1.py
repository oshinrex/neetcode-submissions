class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}
        def dfs(i, tot): 
            if tot == amount: 
                return 1
            if i >= len(coins) or tot > amount:
                return 0
            
            if (i, tot) in dp: 
                return dp[(i, tot)]
            
            dp[(i, tot)] = dfs(i, tot + coins[i]) + dfs(i + 1, tot)
            
            return dp[(i, tot)]
        
        return dfs(0, 0)