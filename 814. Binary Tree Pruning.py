from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        return self.dfs(root)

    def dfs(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        # do postorder
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)

        # process root 
        if not root.left and not root.right:
            return root if root.val == 1 else None
        return root
