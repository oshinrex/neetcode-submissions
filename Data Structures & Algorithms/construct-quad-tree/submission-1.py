"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        if not grid: 
            return None 
        
        def dfs(n, r, c):
            if n == 1: 
                val = True if grid[r][c] == 1 else False
                return Node(val, True, None, None, None, None)
            
            same = True
            for i in range(r, r + n):
                for j in range(c, c + n):
                    if grid[i][j] != grid[r][c]:
                        same = False
                        break 
            
            if same:
                val = True if grid[r][c] == 1 else False
                return Node(val, True, None, None, None, None)

            topLeft = dfs(n // 2, r, c)
            topRight = dfs(n // 2, r, c + n // 2)
            bottomLeft = dfs(n // 2, r + n // 2, c)
            bottomRight = dfs(n // 2, r + n // 2, c + n // 2)

            return Node(False, False, topLeft, topRight, bottomLeft, bottomRight)
        
        return dfs(len(grid), 0, 0)