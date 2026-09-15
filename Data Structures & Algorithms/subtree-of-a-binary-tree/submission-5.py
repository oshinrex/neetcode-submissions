# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(root, subRoot): 
            if not root and not subRoot:
                return True
            
            if not root and subRoot:
                return False
            
            if root and not subRoot:
                return False
            
            if root.val != subRoot.val:
                return False
            
            return isSame(root.left, subRoot.left) and isSame(root.right, subRoot.right)

        def dfs(root, subRoot):
            if not root: 
                return False 

            if isSame(root, subRoot):
                return True 
            
            return dfs(root.left, subRoot) or dfs(root.right, subRoot)
        
        return dfs(root, subRoot)
            