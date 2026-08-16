# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = collections.deque()
        if root:
            q.append(root)

        while q: 
            level = len(q)
            layer = []
            for i in range(level):
                node = q.popleft()
                layer.append(node.val)
                if node.left: 
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(layer)
        
        return res