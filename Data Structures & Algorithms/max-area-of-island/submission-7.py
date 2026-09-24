class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0: 
                return 0 
            
            dir = [(0, 1), (1, 0), (-1, 0), (0, -1)]

            grid[i][j] = 0 

            res = 1

            for x, y in dir: 
                res += dfs(i + x, j + y)
            
            return res 
        
        res = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    res = max(dfs(i, j), res)
        
        return res