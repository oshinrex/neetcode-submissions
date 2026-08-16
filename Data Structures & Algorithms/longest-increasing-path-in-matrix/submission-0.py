class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = {}

        def dfs(i, j): 
            if (i, j) in dp: 
                return dp[(i, j)]
            
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            res = 1
            for x, y in directions: 
                if i+x < len(matrix) and j+y < len(matrix[0]) and i+x >= 0 and j+y >= 0 and matrix[i+x][j+y] > matrix[i][j]:
                    res = max(res, 1 + dfs(i+x, j+y))
            
            dp[(i, j)] = res
            return res 
        
        longest = 0
        for i in range(len(matrix)): 
            for j in range(len(matrix[0])):
                longest = max(longest, dfs(i, j))
        
        return longest