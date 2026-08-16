class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        total_fruit = 0
        row, col = len(grid), len(grid[0])
        q = deque()
        time = 0

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1: 
                    total_fruit += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        # bfs stage 
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = set()
        count = len(q)
        found = 0
        while q: 
            point = q.popleft()
            for d in directions:
                x = point[0] + d[0]
                y = point[1] + d[1]

                if (x >= 0 and x < row and y >= 0 and y < col):
                    if grid[x][y] == 1 and (x, y) not in visited:
                        visited.add((x, y))
                        q.append((x, y))
                        found += 1
            count -= 1
            if count == 0 and len(q) != 0:
                time += 1
                count = len(q)


        
        if total_fruit == found: 
            return time
        else: 
            return -1