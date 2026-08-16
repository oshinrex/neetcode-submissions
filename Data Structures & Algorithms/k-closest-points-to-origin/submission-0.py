class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        ret = []
        heapq.heapify(res)

        for x, y in points: 
            heapq.heappush(res, (x**2 + y**2, [x, y]))
        
        for i in range(k): 
            ret.append(heapq.heappop(res)[1])
        
        return ret
        
        