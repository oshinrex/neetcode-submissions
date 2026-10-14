class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = prices[0]
        res = 0 

        for r in range(1, len(prices)): 
            if prices[r] < min_val: 
                min_val = prices[r]
            else: 
                res = max(res, prices[r] - min_val)
        
        return res