class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = prices[0]
        max_diff = 0 

        for r in range(1, len(prices)): 
            if prices[r] < min_val:
                min_val = prices[r]
            else: 
                max_diff = max(max_diff, prices[r] - min_val)

        return max_diff