class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i, j))
            
        print(q)
        while q:
            i, j = q.popleft()
            
            for x, y in directions:
                ix, jy = i + x, j + y
                if ix < 0 or ix == len(grid) or jy < 0 or jy >= len(grid[0]) or (grid[ix][jy] != 2147483647):
                    continue 
                grid[ix][jy] = grid[i][j] + 1
                q.append((ix, jy))