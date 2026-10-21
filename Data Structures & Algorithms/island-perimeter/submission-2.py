class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        res = 0 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    for x, y in dir: 
                        if i+x < 0 or j+y < 0 or i+x == len(grid) or j+y == len(grid[0]) or grid[i+x][j+y] == 0: 
                            res += 1
        
        return res