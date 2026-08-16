class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid: 
            return 0
        
        row, col = len(grid), len(grid[0])
        maxArea = 0
        visited = set()

        def dfs(i, j): 
            if i < 0 or i >= row or j < 0 or j >= col or grid[i][j] == 0 or (i, j) in visited:
                return 0
            else:
                visited.add((i, j))
                return 1 + dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1)
    
        for i in range(row):
            for j in range(col): 
                if grid[i][j] == 1 and (i, j) not in visited:
                    area = dfs(i, j)
                    maxArea = max(maxArea, area)
        
        return maxArea
