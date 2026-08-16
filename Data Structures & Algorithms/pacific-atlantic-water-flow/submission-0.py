class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row, col = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visited, prev): 
            if r < 0 or c < 0 or r == row or c == col or (r, c) in visited or heights[r][c] < prev: 
                return 
            visited.add((r, c))
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])
        
        for c in range(col): 
            dfs(0, c, pac, heights[0][c])    
            dfs(row - 1, c, atl, heights[row - 1][c])
        
        for r in range(row): 
            dfs(r, 0, pac, heights[r][0])
            dfs(r, col - 1, atl, heights[r][col - 1])
        
        res = []
        for i in range(row):
            for j in range(col):
                if (i, j) in pac and (i, j) in atl: 
                    res.append([i, j])
        
        return res