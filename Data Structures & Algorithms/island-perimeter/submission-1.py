class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()
        per = 0

        def dfs(i, j): 
            nonlocal per 
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
                return False 
            
            if (i, j) in visited: 
                return True 
            
            visited.add((i, j))

            dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]
            for x, y in dir: 
                if not dfs(i + x, j + y): 
                    per += 1
            
            return True 
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1: 
                    dfs(i, j)
        return per 
            