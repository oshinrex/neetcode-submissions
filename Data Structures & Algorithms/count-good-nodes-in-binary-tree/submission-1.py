# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# use dfs, keep track of the largest value you have seen so far, if that is greater, then not true
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, largest): 
            if not root: 
                return 0 

            if root.val >= largest: 
                return 1 + dfs(root.left, root.val) + dfs(root.right, root.val)
            else: 
                return dfs(root.left, largest) + dfs(root.right, largest)
        
        return dfs(root, float("-inf"))

            