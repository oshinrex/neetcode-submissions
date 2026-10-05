class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for p in points:
            x, y = p[0], p[1]
            dist = x**2 + y**2

            if len(heap) == k:
                d, _ = heap[0]
                if -dist <= d:
                    continue 
                else:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (-dist, p))
            else:
                heapq.heappush(heap, (-dist, p))
        
        res = []
        for _, p in heap:
            res.append(p)
        
        return res