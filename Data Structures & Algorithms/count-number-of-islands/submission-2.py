class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: 
            return 0 
        
        numIsland = 0
        visited = set() 
        row, col = len(grid), len(grid[0])

        def bfs(i, j): 
            visited.add((i, j))

            directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
            for x, y in directions: 
                if 0 <= i + x < row and 0 <= j + y < col: 
                    if grid[i + x][j + y] == "1" and (i + x, j + y) not in visited:
                        bfs(i+x, j+y)

        for i in range(row): 
            for j in range(col): 
                if (grid[i][j] == "1" and (i, j) not in visited):
                    bfs(i, j)
                    numIsland += 1
        
        return numIsland