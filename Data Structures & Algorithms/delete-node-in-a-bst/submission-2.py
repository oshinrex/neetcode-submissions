# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: 
            return None 

        def replace(root):
            if not root.left and not root.right: 
                return None 
            elif not root.left: 
                return root.right
            elif not root.right: 
                return root.left
            else: 
                # find the right most left node
                init = root.left
                curr = init
                while curr.right:
                    curr = curr.right 
                
                curr.right = root.right 
                return init 
        
        def res(root):
            if not root: 
                return None 
            
            if root.left and root.left.val == key: 
                root.left = replace(root.left)
                return 

            elif root.right and root.right.val == key: 
                root.right = replace(root.right)
                return
            
            elif key < root.val:
                res(root.left)
            
            else:
                res(root.right)
        
        if root and root.val == key:
            return replace(root)
            
        res(root)
        return root
        