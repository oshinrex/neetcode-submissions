class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def surr(r, c): 
            res = 0 
            for x, y in dir:
                if (x + r) < 0 or (x + r) == len(grid) or (y + c) < 0 or (y + c) == len(grid[0]) or grid[x + r][y + c] == 0:
                    res += 1
            return res

        count = 0 
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    continue 
            
                count += surr(r, c)
        
        return count