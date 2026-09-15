# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: 
            return []
        level = deque()
        level.append(root)
        res = []

        while level: 
            toAdd = []
            for i in range(len(level)):
                curr = level.popleft()
                if curr.left: 
                    level.append(curr.left)
                
                if curr.right:
                    level.append(curr.right)

                toAdd.append(curr.val)
            res.append(toAdd)
        
        return res