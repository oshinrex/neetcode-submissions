# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(max_val, root):
            if not root: 
                return 0 
            
            if root.val < max_val: 
                return dfs(max_val, root.left) + dfs(max_val, root.right)
            else: 
                return 1 + dfs(root.val, root.left) + dfs(root.val, root.right)
        
        return dfs(root.val, root)