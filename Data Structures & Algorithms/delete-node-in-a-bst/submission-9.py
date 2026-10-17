# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # find node 
        curr = root 
        prev = None

        while curr and curr.val != key: 
            prev = curr 
            if key < curr.val: 
                curr = curr.left 
            else: 
                curr = curr.right
        
        if not curr: 
            return root 
        
        # if leaf (prev's child is none)
        if not curr.left and not curr.right: 
            if not prev: 
                return None 

            if prev.val > curr.val: 
                prev.left = None 
            else: 
                prev.right = None 
         
        # if no right node (prev nodes left child is curr.right)
        elif not curr.right: 
            if not prev: 
                return curr.left

            if prev.val > curr.val: 
                prev.left = curr.left 
            else: 
                prev.right = curr.left 
        
        # if has a child (leftmost of right node) - delete leftmost node + put value in curr
        else: 
            print('here')
            p = None
            right = curr.right 

            while right.left: 
                p = right 
                right = right.left 
            
            curr.val = right.val 
            if not p: 
                print('here1')
                curr.right = right.right
            else:
                p.left = right.right 
        
        return root 