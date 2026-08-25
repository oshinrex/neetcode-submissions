class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        heap = []
        heapq.heapify(heap)

        for t in tasks: 
            freq[t] = freq.get(t, 0) + 1
        
        for k in freq: 
            heapq.heappush(heap, (-freq[k], k))
        
        res = 0
        prev = ""
        hold = []
        while heap or hold: 
            while hold: 
                i, p = hold[0]
                if i == res: 
                    heapq.heappush(heap, p)
                    hold.pop(0)
                else: 
                    break 
            
            if heap: 
                freq, val = heapq.heappop(heap)
                if freq + 1 != 0:
                    hold.append((res + n + 1, (freq + 1, val)))
            res += 1
        
        return res

            
            
