# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def helper(root):
            if not root: 
                return (0, 0)
            
            robleft, skipleft = helper(root.left)
            robright, skipright = helper(root.right)

            robThis = root.val + skipleft + skipright 
            skipThis = max(robleft, skipleft) + max(robright, skipright)

            return (robThis, skipThis)
        
        
        v1, v2 = helper(root)

        print(v1)
        print(v2)

        return max(v1, v2)