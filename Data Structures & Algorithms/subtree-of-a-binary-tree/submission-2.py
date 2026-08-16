class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(root, subRoot):
            if not root and not subRoot: 
                return True
            elif not root or not subRoot or root.val != subRoot.val:
                return False
            else:
                return isSame(root.left, subRoot.left) and isSame(root.right, subRoot.right)
        
        if not root:
            return False
        return isSame(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)