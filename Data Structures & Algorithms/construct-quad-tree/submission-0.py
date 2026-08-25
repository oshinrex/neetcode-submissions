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
        
        def dfs(n, r, c): 
            isSame = True
            for i in range(n):
                for j in range(n):
                    if grid[i+r][j+c] != grid[r][c]:
                        isSame = False
                        break 
            
            if isSame: 
                return Node(grid[r][c], True)
            
            topLeft = dfs(n//2, r, c)
            topRight = dfs(n//2, r, c + n//2)
            bottomLeft = dfs(n//2, r + n//2, c)
            bottomRight = dfs(n//2, r + n//2, c + n//2)

            return Node(0, False,topLeft, topRight, bottomLeft, bottomRight)
        
        return dfs(len(grid), 0, 0)
