# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        positions = {value: i for i, value in enumerate(inorder)}
        def helper(i, j, k, l):
            if i > j: 
                return None 
            
            root = preorder[i]
            
            index = positions[root]
            
            left = helper(i + 1, i + index - k, k, index - 1)
            right = helper(i + index - k + 1, j, index + 1, l)

            return TreeNode(root, left, right)
        
        return helper(0, len(preorder) - 1, 0, len(inorder) - 1)