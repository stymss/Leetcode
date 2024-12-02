from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        # Do inorder traversal
        nodes = self.inorderTraversal(root)

        # check for the wrong nodes
        first, second = None, None
        
        for i in range(len(nodes) - 1):
            if nodes[i].val > nodes[i + 1].val:
                if not first:
                    first = nodes[i]
                second = nodes[i + 1]

        # swap the value of these two nodes
        temp = first.val
        first.val, second.val = second.val, temp

    # inorder of BST gives sorted array
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        inorder, stack = [], []
        if not root:
            return []
        
        while stack or root:
            while root:
                stack.append(root)
                root = root.left 

            root = stack.pop()
            inorder.append(root)
            root = root.right 
        return inorder
