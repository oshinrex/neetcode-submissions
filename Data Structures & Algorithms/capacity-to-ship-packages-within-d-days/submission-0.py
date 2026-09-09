class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)

        while l <= r: 
            max_weight = (l + r) // 2
            print("max_weight: " + str(max_weight))

            d = 0 
            curr_weight = 0
            failed = False
            for w in weights: 
                if curr_weight + w <= max_weight: 
                    curr_weight += w
                else: 
                    if d + 1 < days:
                        d += 1
                        curr_weight = w
                    else: 
                        failed = True 
                        break 
            
            if failed: 
                l = max_weight + 1
                print("failed: l, " + str(l) + " r, " + str(r))
            else: 
                r = max_weight - 1
                print("success: l, " + str(l) + " r, " + str(r))

        return l 