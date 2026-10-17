# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def subroot(root, subRoot):
            if not subRoot and not root: 
                return True 
            
            if (not subRoot and root) or (subRoot and not root):
                return False
            
            if root.val != subRoot.val:
                return False
            
            return subroot(root.left, subRoot.left) and subroot(root.right, subRoot.right)
        
        def dfs(root):
            if not root: 
                return False 
            
            return subroot(root, subRoot) or dfs(root.left) or dfs(root.right)
        
        return dfs(root)