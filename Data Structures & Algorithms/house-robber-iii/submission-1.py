# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        visited = {}
        def helper(root):
            if not root: 
                return 0 
            
            if root in visited: 
                return visited[root]

            res1 = 0 
            res2 = 0 
            if root.left:
                res1 += helper(root.left)
                res2 += helper(root.left.left) + helper(root.left.right)

            if root.right: 
                res1 += helper(root.right)
                res2 += helper(root.right.left) + helper(root.right.right)

            root.val = max(res1, res2 + root.val)
            visited[root] = root.val
            return root.val 
        
        return helper(root)