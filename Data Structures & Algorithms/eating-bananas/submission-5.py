class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_rate = 0

        for i in range(len(piles)):
            max_rate = max(max_rate, piles[i])
        
        l = 1
        r = max_rate
        ret = max_rate

        while (l <= r): 
            hours = 0
            mid = (l + r) // 2
            for i in range(len(piles)):
                hours += (piles[i] // mid)
                if piles[i] % mid != 0:
                    hours += 1
            if hours <= h: 
                ret = min(ret, mid)
                r = mid - 1
            else: 
                l = mid + 1

        return ret
        
