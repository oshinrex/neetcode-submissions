class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh_fruit = 0 
        rotten_fruit = 0 
        rotten_q = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    continue 
                elif grid[i][j] == 1: 
                    fresh_fruit += 1
                else: 
                    rotten_fruit += 1
                    rotten_q.append((i, j))
        
        seen = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        time = 0 

        while rotten_q and fresh_fruit != 0: 
            for _ in range(len(rotten_q)):
                i, j = rotten_q.popleft()

                for x, y in directions:
                    ix, jy = i + x, j + y
                    if ix < 0 or ix == len(grid) or jy < 0 or jy == len(grid[0]) or (ix, jy) in seen or grid[ix][jy] != 1:
                        continue 
                    seen.add((ix, jy))
                    fresh_fruit -= 1
                    rotten_q.append((ix, jy))
            time += 1
        
        
        return time if fresh_fruit == 0 else -1