class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0 
        visited = set()

        def dfs(i, j): 
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == "0" or (i, j) in visited:
                return
            
            grid[i][j] = "0"

            dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for x, y in dir: 
                dfs(i + x, j + y)
            
            return True 

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    num_islands += 1
                    dfs(i, j)
        
        return num_islands
            