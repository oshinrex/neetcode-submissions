class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0 
        seen = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(i, j): 
            if (i, j) in seen or i < 0 or j < 0 or i == len(grid) or j == len(grid[0]) or grid[i][j] == 0:
                return 0 
            
            res = 1
            seen.add((i, j))

            for x, y in directions: 
                res += dfs(i + x, j + y)

            return res 
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in seen: 
                    max_area = max(max_area, dfs(i, j))
        
        return max_area