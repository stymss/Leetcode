from typing import Optional, Dict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
class Solution:
    def markParents(self, root: Optional[TreeNode], parentMap: Dict[TreeNode, TreeNode]):
        q = deque([root])
        while q:
            root = q.popleft()
            if root.left:
                parentMap[root.left] = root
                q.append(root.left)

            if root.right:
                parentMap[root.right] = root
                q.append(root.right)

    def findNode(self, root: Optional[TreeNode], start:int) -> Optional[TreeNode]:
        if not root:
            return None 
        
        if root.val == start:
            return root 
        
        # search in both the left and right subtrees
        left = self.findNode(root.left, start)
        right = self.findNode(root.right, start)
        return left or right

    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        if not root:
            return 0
        
        parentMap = dict()
        # Note - root node has no parent
        self.markParents(root, parentMap)

        # visited to track nodes which has been visited
        visited = set() 

        # find the node with the given start value
        start_node = self.findNode(root, start)

        # mark the start node as visited, add to queue and mark time as 0
        q = deque([start_node])
        visited.add(start_node)
        time_to_infect = 0

        # do BFS
        while q:
            time_to_infect += 1
            for i in range(len(q)):
                node = q.popleft()

                # check all it's children and parent
                if node.left is not None and node.left not in visited:
                    q.append(node.left)
                    visited.add(node.left)

                if node.right is not None and node.right not in visited:
                    q.append(node.right)
                    visited.add(node.right)

                if parentMap.get(node) is not None and parentMap.get(node) not in visited:
                    q.append(parentMap[node])
                    visited.add(parentMap[node])

        return time_to_infect-1
