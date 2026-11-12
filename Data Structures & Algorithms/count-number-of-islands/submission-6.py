class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0 
        seen = set()
        dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(i, j): 
            nonlocal seen
            nonlocal dir 

            if (i, j) in seen or i < 0 or j < 0 or i == len(grid) or j == len(grid[0]) or grid[i][j] == "0":
                return 
            
            seen.add((i, j))
            for x, y in dir: 
                dfs(i + x, j + y)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in seen and grid[i][j] == "1":
                    islands += 1
                    dfs(i, j)
        
        return islands