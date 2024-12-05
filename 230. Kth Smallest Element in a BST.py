from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inorder = self.inorder(root)
        return inorder[k-1]
    
    def inorder(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        stack, inorder = [], []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            inorder.append(root.val)
            root = root.right
        return inorder

