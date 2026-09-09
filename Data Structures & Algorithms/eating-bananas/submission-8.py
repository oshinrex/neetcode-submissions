class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        min_rate = r
        
        while l <= r:
            mid = (l + r) // 2

            count = 0
            for p in piles: 
                count += p // mid
                if p % mid != 0: 
                    count += 1
            
            if count <= h: 
                min_rate = min(min_rate, mid)
                r = mid - 1
            else: 
                l = mid + 1
        
        return min_rate