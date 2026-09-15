# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: 
            return []
        res = []
        level = deque()
        level.append(root)

        while level: 
            res.append(level[-1].val)

            for i in range(len(level)): 
                curr = level.popleft()
                if curr.left:
                    level.append(curr.left)
                
                if curr.right:
                    level.append(curr.right)
            
        return res 
