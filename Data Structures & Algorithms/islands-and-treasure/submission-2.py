class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        row, col = len(grid), len(grid[0])

        def dfs(i, j, val): 
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for x, y in directions: 
                if 0 <= i + x < row and 0 <= j + y < col and grid[i + x][y + j] >= val + 1:
                    grid[i + x][j + y] = val + 1
                    dfs(i + x, j + y, val + 1)

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    dfs(i, j, 0)
        