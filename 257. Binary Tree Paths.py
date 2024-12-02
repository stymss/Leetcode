from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # TC -> O(n * h) n for each node in the tree and h for path creation (h is the height of tree)
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []

        paths = []
        self.getPaths(root, paths, "")
        return paths

    def getPaths(self, root: Optional[TreeNode], paths: List[str], path: str) -> None:
        # If there is no root, return
        if not root:
            return 
        
        # Add the current node to path
        path += str(root.val)
        path += "->"

        # Check if leaf
        if not root.left and not root.right:
            # add path to paths as we have reached leaf
            path = path[:-2]
            paths.append(path) 
        
        # Explore left and right side of root
        self.getPaths(root.left, paths, path)
        self.getPaths(root.right, paths, path)
        

##### Optimised #######
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # TC -> O(n), where n is the number of nodes in the tree
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        
        paths = []
        self.getPaths(root, paths, [])
        return paths

    def getPaths(self, root: Optional[TreeNode], paths: List[str], path: List[int]) -> None:
        if not root:
            return 
        
        # Add the current node to the path
        path.append(root.val)

        # If it's a leaf node, add the current path to paths
        if not root.left and not root.right:
            paths.append("->".join(map(str, path)))
        else:
            # Otherwise, explore the left and right children
            self.getPaths(root.left, paths, path.copy())
            self.getPaths(root.right, paths, path.copy())
