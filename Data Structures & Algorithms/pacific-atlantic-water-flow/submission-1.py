class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac = set() 
        atl = set() 
        res = []

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
        def dfs(i, j, visited): 
            visited.add((i, j))

            for x, y in directions: 
                if (i + x < 0 or j + y < 0 or i + x >= len(heights) or j + y >= len(heights[0]) or (i + x, j + y) in visited or heights[i + x][j + y] < heights[i][j]):
                    continue  
                dfs(i + x, j + y, visited)
 
        
        for i in range(len(heights[0])): 
            dfs(0, i, pac)
            dfs(len(heights) - 1, i, atl)
        
        for j in range(len(heights)):
            dfs(j, 0, pac)
            dfs(j, len(heights[0]) - 1, atl)
        
        res = []

        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if (i, j) in atl and (i, j) in pac: 
                    res.append((i, j))
        
        return res