class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: 
            return 0

        islands = 0
        r, c = len(grid), len(grid[0])
        visited = set()

        def bfs(i, j):
            if (grid[i][j] == "1" and (i, j) not in visited):
                visited.add((i, j))
                if (i + 1 < r):
                    bfs(i+1, j)
                if (j + 1 < c):
                    bfs(i, j+1)
                if (i - 1 >= 0):
                    bfs(i - 1, j)
                if (j - 1 >= 0):
                    bfs(i, j - 1)

        for i in range(r):
            for j in range(c):
                if (grid[i][j] == "1" and (i, j) not in visited):
                    islands += 1
                    bfs(i, j)
        
        return islands