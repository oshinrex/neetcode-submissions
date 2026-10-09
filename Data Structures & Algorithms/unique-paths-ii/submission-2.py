class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or obstacleGrid[0][0] == 1 or obstacleGrid[len(obstacleGrid) - 1][len(obstacleGrid[0]) - 1]:
            return 0

        # dp: dp[i][j] = whether or not it has reached the end
        res = 0 
        dp = {}

        def backtrack(i, j):
            nonlocal res
            if (i, j) in dp: 
                return dp[(i, j)]
            
            if i == len(obstacleGrid) - 1 and j == len(obstacleGrid[0]) - 1:
                return 1 
            
            if i >= len(obstacleGrid) or j >= len(obstacleGrid[0]) or obstacleGrid[i][j] == 1:
                return 0
            
            dp[(i + 1, j)] = backtrack(i + 1, j)
            dp[(i, j + 1)] = backtrack(i, j + 1)

            dp[(i, j)] = dp[(i + 1, j)] + dp[(i, j + 1)]
            return dp[(i, j)]
        
        return backtrack(0, 0)
            


