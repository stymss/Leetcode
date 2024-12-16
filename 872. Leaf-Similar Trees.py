from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaves1, leaves2 = [], []
        self.getLeaves(root1, leaves1)
        self.getLeaves(root2, leaves2)
        return leaves1 == leaves2

    def getLeaves(self, root, leaves):
        if not root:
            return leaves

        if not root.left and not root.right:
            leaves.append(root.val)
            return

        self.getLeaves(root.left, leaves)
        self.getLeaves(root.right, leaves)
        