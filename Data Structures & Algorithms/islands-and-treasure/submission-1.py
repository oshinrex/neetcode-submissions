class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row, col = len(grid), len(grid[0])
        q = deque()
        visited = set()
        layer = 0

        for i in range(row): 
            for j in range(col):
                if grid[i][j] == 0:
                    q.append((i, j))

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        count = len(q)
        while q: 
            print(q)
            curr = q.popleft()
            count -= 1
            for d in directions: 
                x = d[0] + curr[0]
                y = d[1] + curr[1]
                
                if (x >= 0 and x < row and y >= 0 and y < col):
                    if (grid[x][y] == 2147483647 and (x, y) not in visited):
                        grid[x][y] = layer + 1
                        visited.add((x, y))
                        q.append((x, y))
                        print(x)
                        print(y)
            if count == 0:
                layer += 1
                count = len(q)
        
                
            