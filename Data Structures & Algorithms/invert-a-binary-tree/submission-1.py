# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if (root != None):
            temp = root.left
            root.left = root.right 
            root.right = temp 

            self.helper(root.left)
            self.helper(root.right)
        
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        head = root
        self.helper(head)
        return head