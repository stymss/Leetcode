from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Function to check if both subtrees are same or not
    def isTreeSym(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if not p or not q:
            return False

        return True if p.val == q.val and self.isTreeSym(p.left, q.right) and self.isTreeSym(p.right, q.left) else False
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True 

        return self.isTreeSym(root.left, root.right)
     