class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row, col = len(grid), len(grid[0])
        chests = deque()

        # find all treasure chests
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    chests.append((i, j))
        
        while chests:
            i, j = chests.popleft()
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            for x, y in directions: 
                if i + x < 0 or i + x >= row or j + y < 0 or j + y >= col or grid[i+x][j+y] != 2147483647: 
                    continue
                grid[i+x][j+y] = grid[i][j] + 1
                chests.append((i+x, j+y))

