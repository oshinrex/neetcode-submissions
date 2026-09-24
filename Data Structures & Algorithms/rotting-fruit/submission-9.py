class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0 
        rotten = 0
        q = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1: 
                    fresh += 1
                
                if grid[i][j] == 2:
                    rotten += 1
                    q.append((i, j))
        
        time = 0 
        dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while q: 
            for i in range(len(q)): 
                x, y = q.popleft()

                for a, b in dir: 
                    cx = x + a 
                    cy = y + b 
                    if cx < 0 or cx >= len(grid) or cy < 0 or cy >= len(grid[0]) or grid[cx][cy] != 1:
                        continue 
                    grid[cx][cy] = 2
                    fresh -= 1
                    q.append((cx, cy))
            print(q)

            if len(q):
                time += 1
        
        print(fresh)
        print(grid)
        if fresh != 0: 
            return -1
        else:
            return time
