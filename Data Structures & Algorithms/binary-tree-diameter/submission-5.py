# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiam = 0 
        def height(root): 
            if not root: 
                return 0 
            
            return 1 + max(height(root.left), height(root.right))
        
        def dfs(root): 
            nonlocal maxDiam 
            if not root: 
                return
            maxDiam = max(maxDiam, height(root.right) + height(root.left))
            print("maxDiam: " + str(maxDiam))
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        return maxDiam