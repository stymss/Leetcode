from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 0)

    def dfs(self, root: Optional[TreeNode], current_sum) -> int:
        if not root:
            return 0

        current_sum = current_sum * 10 + root.val

        if not root.left and not root.right:
            return current_sum

        sum_left = self.dfs(root.left, current_sum)
        sum_right = self.dfs(root.right, current_sum)

        return sum_left + sum_right