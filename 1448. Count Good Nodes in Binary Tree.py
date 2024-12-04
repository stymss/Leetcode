# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        return self.countGoodNodes(root, root.val)
    
    def countGoodNodes(self, root: TreeNode, max_so_far: int) -> int:
        if not root:
            return 0
        
        # declaration
        good_nodes = 0
        # get the maximum value seen so far
        max_so_far = max(max_so_far, root.val)

        # check if the current node is a good node or not
        if root.val >= max_so_far:
            good_nodes += 1

        # check in both left and right side
        good_nodes_in_left = self.countGoodNodes(root.left, max_so_far)
        good_nodes_in_right = self.countGoodNodes(root.right, max_so_far)

        return good_nodes + good_nodes_in_left + good_nodes_in_right
