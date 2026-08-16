class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        time = 0
        row, col = len(grid), len(grid[0])
        layer = 0

        for i in range(row):
            for j in range(col): 
                if grid[i][j] == 2: 
                    q.append((i, j))
        
        layer = len(q)
        
        while q: 
            if layer == 0: 
                time += 1
                layer = len(q)
            i, j = q.popleft()
            layer -= 1
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for x, y in directions: 
                
                if x+i < 0 or x+i >= row or y+j < 0 or y+j >= col or grid[x+i][y+j] == 0 or grid[x+i][y+j] == 2:
                    continue
                grid[x+i][y+j] = 2
                q.append((x+i, y+j))
                
        
        for i in range(row): 
            for j in range(col): 
                if grid[i][j] == 1:
                    return -1

        return time
            