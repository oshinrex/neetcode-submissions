class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid: 
            return 0
        
        max_area = 0
        visited = set()
        row, col = len(grid), len(grid[0])

        def dfs(r, c):
            ret = 1
            visited.add((r, c))
            q = deque()
            q.append((r, c))

            while q: 
                r, c = q.popleft()
                direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

                for x, y in direction: 
                    if r + x < row and r + x >= 0 and c + y < col and c + y >= 0:
                        if grid[x + r][y + c] == 1 and (x+r, y+c) not in visited:
                            ret += 1
                            q.append((x+r, y+c))
                            visited.add((x+r, y+c))
            
            return ret 


        for r in range(row):
            for c in range(col): 
                if (grid[r][c] == 1 and (r, c) not in visited):
                    area = dfs(r, c)
                    print(area)
                    max_area = max(area, max_area)
        
        return max_area