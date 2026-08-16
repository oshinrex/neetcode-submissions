class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if not points: 
            return 0
        
        visited = set()
        dist = 0
        minHeap = [(0, points[0])]
        heapq.heapify(minHeap)

        while len(visited) < len(points) and minHeap:
            val, point = heapq.heappop(minHeap)
            x, y = point[0], point[1]

            if (x, y) in visited:
                continue
            
            visited.add((x, y))
            dist += val
            
            for p in points:
                x2, y2 = p[0], p[1]
                if (x2, y2) in visited:
                    continue
                d = abs(x - x2) + abs(y - y2)
                heapq.heappush(minHeap, (d, (x2, y2)))
        
        return dist
            
            


