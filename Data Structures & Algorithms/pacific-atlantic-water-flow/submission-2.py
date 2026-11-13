class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        seen_p = set()
        seen_a = set()

        if not heights:
            return []

        pacific = set()
        p_q = deque()

        atlantic = set()
        a_q = deque()

        for i in range(len(heights)):
            pacific.add((i, 0))
            atlantic.add((i, len(heights[0]) - 1))
            

        for j in range(len(heights[0])):
            pacific.add((0, j))
            atlantic.add((len(heights) - 1, j))
        
        for p in pacific:
            p_q.append(p)
        
        for a in atlantic:
            a_q.append(a)
        
        while p_q: 
            i, j = p_q.popleft()
            
            for x, y in directions: 
                ix, jy = i + x, j + y 
                if ix < 0 or jy < 0 or ix == len(heights) or jy == len(heights[0]) or (ix, jy) in seen_p or heights[ix][jy] < heights[i][j]:
                    continue
                
                seen_p.add((ix, jy))
                p_q.append((ix, jy))
                pacific.add((ix, jy))
            
        while a_q: 
            i, j = a_q.popleft()
        
            for x, y in directions: 
                ix, jy = i + x, j + y 
                if ix < 0 or jy < 0 or ix == len(heights) or jy == len(heights[0]) or (ix, jy) in seen_a or heights[ix][jy] < heights[i][j]:
                    continue
                
                seen_a.add((ix, jy))
                a_q.append((ix, jy))
                atlantic.add((ix, jy))

        res = []

        for a in atlantic:
            if a in pacific:
                x, y = a
                res.append([x, y])
        
        return res