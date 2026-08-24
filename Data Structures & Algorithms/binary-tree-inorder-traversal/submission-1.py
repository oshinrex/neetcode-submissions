# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def traverse(head): 
            nonlocal res
            if head is None: 
                return 
            
            traverse(head.left)
            res.append(head.val)
            traverse(head.right)
        
        traverse(root)
        return res