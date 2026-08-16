class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        time = 0
        visited = set()

        minHeap = [(grid[0][0], 0, 0)]
        heapq.heapify(minHeap)

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while minHeap:
            t, i, j = heapq.heappop(minHeap)

            if (i, j) in visited:
                continue 
            visited.add((i, j))

            if i == n - 1 and j == n - 1: 
                return t  

            for x, y in directions: 
                if x + i < 0 or x + i >= n or y + j < 0 or y + j >= n or (x + i, y + j) in visited:
                    continue
                heapq.heappush(minHeap, (max(t, grid[i+x][j+y]), i+x, y+j))
        
