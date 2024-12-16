from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        if not subRoot:
            return True

        # cases
        if root.val == subRoot.val and self.isSameTree(root.left, subRoot.left) and self.isSameTree(root.right, subRoot.right):
            return True

        left_search = self.isSubtree(root.left, subRoot)
        right_search = self.isSubtree(root.right, subRoot)

        return left_search or right_search
        
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False

        return True if p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) else False