from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # TC - O(n)
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        inorder, stack = [], []
        if not root:
            return []
        
        while stack or root:
            while root:
                stack.append(root)
                root = root.left 

            root = stack.pop()
            inorder.append(root.val)
            root = root.right 
        return inorder
