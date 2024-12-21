from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder - root, left, right
        # inorder - left root right

        if not preorder or not inorder:
            return None
            
        root_val = preorder[0]
        root = TreeNode(root_val)
        inorder_idx = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:inorder_idx+1], inorder[:inorder_idx])
        root.right = self.buildTree(preorder[inorder_idx+1:], inorder[inorder_idx+1:])

        return root