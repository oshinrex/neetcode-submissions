# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = None

        def helper(root, m):
            nonlocal res 

            if not root: 
                return m

            stack = []
            curr = root

            while curr: 
                print(curr.val)
                stack.append(curr)
                curr = curr.left 
            
            while stack and m != 0:
                last = stack.pop()
                print(last.val)
                m -= 1
                if m == 0:
                    res = last.val 
                    return m

                m = helper(last.right, m)
            
            return m
        
        helper(root, k)
        return res


