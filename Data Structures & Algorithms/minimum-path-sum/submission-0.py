class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = {}
        def backtrack(i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                return float('inf')
            
            if (i, j) in dp:
                return dp[(i, j)]
            
            if i == len(grid) - 1 and j == len(grid[0]) - 1:
                return grid[len(grid) - 1][len(grid[0]) - 1]
            
            dir = [(1, 0), (0, 1)]

            res = float('inf')
            for x, y in dir: 
                res = min(res, grid[i][j] + backtrack(i + x, j + y))
            dp[(i, j)] = res
            
            return res 
        
        return backtrack(0, 0)
        