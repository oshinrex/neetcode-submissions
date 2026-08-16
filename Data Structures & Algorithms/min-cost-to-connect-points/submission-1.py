class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if not points: 
            return 0
        
        visited = set()
        dist = 0
        minHeap = [(0, 0)]
        heapq.heapify(minHeap)

        while len(visited) < len(points) and minHeap:
            val, point = heapq.heappop(minHeap)
            x, y = points[point][0], points[point][1]

            if point in visited:
                continue
            
            visited.add(point)
            dist += val
            
            for i in range(len(points)):
                if i in visited:
                    continue
                x2, y2 = points[i][0], points[i][1]
                d = abs(x - x2) + abs(y - y2)
                heapq.heappush(minHeap, (d, i))
        
        return dist
            
            


