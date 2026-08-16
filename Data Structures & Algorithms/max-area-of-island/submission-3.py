class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid: 
            return 0
        
        max_area = 0
        visited = set()

        def bfs(i, j):
            visited.add((i, j))

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            sum = 0
            for dx, dy in directions: 
                if 0 <= i + dx < len(grid) and 0 <= j + dy < len(grid[0]) and grid[i + dx][j + dy] == 1 and (i + dx, j + dy) not in visited: 
                    sum += 1 + bfs(i + dx, j + dy)
            
            return sum
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in visited:
                    max_area = max(max_area, 1 + bfs(i, j))
        
        return max_area
        
