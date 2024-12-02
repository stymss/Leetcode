from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val

class Solution:
    # TC - O(n)
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if not p or not q:
            return False

        return True if p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) else False