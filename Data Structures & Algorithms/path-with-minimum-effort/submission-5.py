class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        dist = [[float('inf') for _ in range(len(heights[0]))] for _ in range(len(heights))]
        dist[0][0] = 0 

        heap = []
        heapq.heappush(heap, (0, 0, 0))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while heap: 
            effort, i, j = heapq.heappop(heap)
            
            for dx, dy in directions:
                x, y = i + dx, j + dy 

                if x < 0 or y < 0 or x == len(heights) or y == len(heights[0]):
                    continue 
                
                if dist[x][y] > max(effort, abs(heights[x][y] - heights[i][j])):
                    dist[x][y] = max(effort, abs(heights[x][y] - heights[i][j]))
                    heapq.heappush(heap, (dist[x][y], x, y))
        
        print(dist)
        return dist[len(heights) - 1][len(heights[0]) - 1]
            
        