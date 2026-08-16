class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = 0

        max_pile = 0
        for i in range(len(piles)):
            max_pile = max(max_pile, piles[i])
        
        l, r = 1, max_pile

        while l <= r:
            mid = (l + r) // 2
            tot = 0
            
            for i in range(len(piles)):
                tot += piles[i] // mid
                if piles[i] % mid != 0:
                    tot += 1
            
            if tot <= h: 
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return res
