class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curBuy, curSell = 0, 0
        nextBuy, nextSell = 0, 0

        for i in range(len(prices) - 1, -1, -1): 
            curBuy = max(nextBuy, -prices[i] + nextSell)
            curSell = max(nextSell, prices[i] + nextBuy)
        
            nextBuy = curBuy
            nextSell = curSell
        
        return curBuy