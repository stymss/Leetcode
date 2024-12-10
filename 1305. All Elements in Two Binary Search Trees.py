from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        inorder_root1, inorder_root2 = self.inorder(root1), self.inorder(root2)

        # merge both together
        output = [0]*(len(inorder_root1) + len(inorder_root2))
        i, j, k =  len(inorder_root1)-1, len(inorder_root2)-1, (len(inorder_root1) + len(inorder_root2))-1

        while i >= 0 and j >= 0:
            if inorder_root1[i] >= inorder_root2[j]:
                output[k] = inorder_root1[i]
                i-=1
            else:
                output[k] = inorder_root2[j]
                j-=1
            k-=1

        # Check for remaining
        while i >= 0:
            output[k] = inorder_root1[i]
            i-=1
            k-=1

        while j >= 0:
            output[k] = inorder_root2[j]
            j-=1
            k-=1
        
        return output

    def inorder(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        inorder, stack = [], []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            inorder.append(root.val)
            root = root.right 
        return inorder