class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 
        r = 1
        max_price = 0

        while r < len(prices): 
            if prices[l] >= prices[r]: 
                l = r
                r += 1
            else: 
                max_price = max(max_price, prices[r] - prices[l])
                r += 1
        
        return max_price

                