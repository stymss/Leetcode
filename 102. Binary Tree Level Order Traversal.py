from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        # append to q 
        q = deque([root])

        # levels hold the answer
        levels = []

        while q:
            level = []

            # check all nodes at this level
            for i in range(len(q)):
                root = q.popleft()
                level.append(root.val)

                if root.left:
                    q.append(root.left)
                if root.right:
                    q.append(root.right)

            levels.append(level)
        return levels
                