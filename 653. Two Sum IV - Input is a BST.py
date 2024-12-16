from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        return self.dfs(root, k, set())

    def dfs(self, root, k, seen) -> bool:
        if not root:
            return False

        goal = k-root.val
        if goal in seen:
            return True
        seen.add(root.val)

        return self.dfs(root.left, k, seen) or self.dfs(root.right, k, seen)