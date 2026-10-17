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
        
        def helper(x1, y1, length):
            if length == 1:
                return Node(grid[x1][y1], True)

            p1 = [x1, y1]
            p3 = [x1 + length // 2, y1]
            p2 = [x1, y1 + length // 2]
            p4 = [x1 + length // 2, y1 + length // 2]

            print(p1)
            print(p2)
            print(p3)
            print(p4)

            same = True
            if grid[p1[0]][p1[1]] == grid[p2[0]][p2[1]] == grid[p3[0]][p3[1]] == grid[p4[0]][p4[1]]:
                val = grid[x1][y1]
                for i in range(x1, x1 + length):
                    for j in range(y1, y1 + length):
                        if val != grid[i][j]:
                            same = False
                            break 
            else:
                same = False 
            
            if same: 
                return Node(grid[x1][y1], True)
            
            topLeft = helper(p1[0], p1[1], length // 2)
            topRight = helper(p2[0], p2[1], length // 2)
            bottomLeft = helper(p3[0], p3[1], length // 2)
            bottomRight = helper(p4[0], p4[1], length // 2)

            return Node(0, False, topLeft, topRight, bottomLeft, bottomRight)
        
        return helper(0, 0, len(grid))