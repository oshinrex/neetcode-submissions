class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        heapq.heapify(heap)
        
        for s in stones: 
            heapq.heappush(heap, -s)
        
        while len(heap) > 1: 
            f = -heapq.heappop(heap)
            s = -heapq.heappop(heap)

            if f != s: 
                heapq.heappush(heap, -abs(f - s))
        
        if not heap:
            return 0 
        else: 
            return -heap[0]
