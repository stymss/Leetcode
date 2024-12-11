from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        paths = []
        self.getPaths(root, targetSum, paths, [])
        return paths

    def getPaths(self, root, targetSum, paths, temp) -> None:
        if not root:
            return paths

        targetSum -= root.val
        temp.append(root.val)
        if not root.left and not root.right and targetSum == 0:
            paths.append(temp[:])
            return 

        left = self.getPaths(root.left, targetSum, paths, temp.copy())
        right = self.getPaths(root.right, targetSum, paths, temp.copy())

        return left and right
