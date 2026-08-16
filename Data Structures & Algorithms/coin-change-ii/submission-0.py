class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}
        def dfs(i, tot): 
            if tot == amount: 
                return 1
            if i >= len(coins) or tot > amount:
                return 0
            
            if (i, tot + coins[i]) not in dp:
                dp[(i, tot + coins[i])] = dfs(i, tot + coins[i])
            
            if (i + 1, tot) not in dp: 
                dp[(i + 1, tot)] = dfs(i + 1, tot)
            
            return dp[(i, tot + coins[i])] + dp[(i + 1, tot)]
        
        return dfs(0, 0)