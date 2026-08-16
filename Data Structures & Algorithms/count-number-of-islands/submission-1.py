class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: 
            return 0
        
        row, col = len(grid), len(grid[0])
        num_islands = 0
        visited = set()

        def bfs(i, j):
            visited.add((i, j))
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for x, y in directions: 
                if 0 <= x + i < row and 0 <= y + j < col and grid[x+i][y+j] == "1" and (x+i, y+j) not in visited: 
                    bfs(x+i, y+j)

        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1" and (i, j) not in visited:
                    bfs(i, j)
                    num_islands += 1
        
        return num_islands