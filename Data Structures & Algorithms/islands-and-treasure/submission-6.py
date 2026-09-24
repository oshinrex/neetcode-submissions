class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0: 
                    q.append((i, j))
        
        dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        while q: 
            i, j = q.popleft()

            for x, y in dir: 
                if i + x < 0 or i + x >= len(grid) or j + y < 0 or j + y >= len(grid[0]) or grid[i + x][j + y] == -1 or grid[i + x][j + y] < (2**31 - 1):
                    continue 
                else:  
                    grid[i + x][j + y] = grid[i][j] + 1
                    q.append((i + x, j + y))
        
