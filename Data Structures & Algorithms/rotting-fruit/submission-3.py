class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh, rotting = 0, 0
        time = 0 
        q = deque()
        row, col = len(grid), len(grid[0])

        for i in range(len(grid)): 
            for j in range(len(grid[0])): 
                if grid[i][j] == 1: 
                    fresh += 1
                    continue
                if grid[i][j] == 2:
                    q.append((i, j))
        
        layer = len(q)
        while q: 
            i, j = q.popleft()
            layer -= 1
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for x, y in directions: 
                if x+i < 0 or x+i >= row or y+j<0 or y+j >= col or grid[x+i][y+j] != 1: 
                    continue
                q.append((x+i, y+j))
                fresh -= 1
                grid[x+i][y+j] = 2
            if layer == 0 and q: 
                time += 1
                layer = len(q)
        
        if fresh == 0: 
            return time
        else: 
            return -1

