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
            
            m = max(max_val, root.val)
            return (1 if max_val <= root.val else 0) + dfs(m, root.left) + dfs(m, root.right)
        return dfs(root.val, root)