class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
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
        
        while q and fresh != 0: 
            for _ in range(len(q)):
                i, j = q.popleft()
                directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                for x, y in directions: 
                    if x+i < 0 or x+i >= row or y+j<0 or y+j >= col or grid[x+i][y+j] != 1: 
                        continue
                    q.append((x+i, y+j))
                    fresh -= 1
                    grid[x+i][y+j] = 2
            time += 1
            
        
        return time if fresh == 0 else -1

