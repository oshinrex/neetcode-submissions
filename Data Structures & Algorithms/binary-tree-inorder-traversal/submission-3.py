# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # inorder: left, center, right 
        res = []

        def helper(node):
            nonlocal res 

            if not node: 
                return None 
            
            helper(node.left)
            res.append(node.val)
            helper(node.right)
    
        helper(root)
        return res