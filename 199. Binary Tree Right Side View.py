from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Base Case
        if not root:
            return []
        
        q = deque([root])
        right_data = [] # To hold the right view of the tree

        while q:
            level_data = []
            for _ in range(len(q)):
                root = q.popleft()
                level_data.insert(0, root.val)

                if root.left:
                    q.append(root.left)
                if root.right:
                    q.append(root.right)
            right_data.append(level_data[0])
        return right_data