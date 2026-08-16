# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if (root is None):
            return False
        else: 
            if (self.equate(root, subRoot)):
                return True
            else:
                return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def equate(self, node, subRoot):
        if (node is None or subRoot is None):
            if (node is None and subRoot is None):
                return True
            else: 
                return False
        
        if (node.val == subRoot.val):
            return self.equate(node.left, subRoot.left) and self.equate(node.right, subRoot.right)
        else:
            return False


