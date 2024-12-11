from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return root

        stack = []
        stack.append(root)
        # Do preorder traversal of the tree
        while stack:
            root = stack.pop()

            # Append right child
            if root.right:
                stack.append(root.right)

            # Append left child
            if root.left:
                stack.append(root.left)

            if stack:
                # Get the top element
                root.right = stack[-1]
                root.left = None
        