# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: 
            return []
        
        res = []
        q = deque()
        q.append(root)

        while q: 
            level = [0] * len(q)
            for i in range(len(level)):
                curr = q.popleft()
                level[i] = curr.val
                if curr.left:
                    q.append(curr.left)
                
                if curr.right:
                    q.append(curr.right)
            res.append(level)
        
        return res