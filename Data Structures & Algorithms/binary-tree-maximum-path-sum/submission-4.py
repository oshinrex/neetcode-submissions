# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        path = root.val

        def dfs(root):
            nonlocal path 
            if not root: 
                return 0 

            left = dfs(root.left)
            right = dfs(root.right)

            path = max(path, root.val, root.val + left, root.val + right, root.val + left + right) 
            return max(root.val, root.val + left, root.val + right)
        
        dfs(root)
        return path
