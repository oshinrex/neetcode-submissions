class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        heapq.heapify(res)

        for x, y in points:
            if len(res) < k: 
                heapq.heappush(res, (-(x**2 + y**2), [x, y]))
            else: 
                if -1 * res[0][0] > x**2 + y**2: 
                    heapq.heappop(res)
                    heapq.heappush(res, (-(x**2 + y**2), [x, y]))
        
        return [p for _, p in res]
        
        