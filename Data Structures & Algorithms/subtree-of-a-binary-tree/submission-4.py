# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same(p, q): 
            if p is None and q is None: 
                return True 
            
            if p is None or q is None or p.val != q.val: 
                return False
            
            return same(p.left, q.left) and same(p.right, q.right)
        
        def isSub(p, q):
            if p is None:
                return False 
                
            return same(p, q) or isSub(p.left, q) or isSub(p.right, q)
        
        return isSub(root, subRoot)