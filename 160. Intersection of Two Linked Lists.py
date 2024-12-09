from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lengthA, lengthB = self.getLength(headA), self.getLength(headB)

        # Get both lists to the same length
        if lengthA > lengthB:
            for _ in range(lengthA - lengthB):
                headA = headA.next
        else:
            for _ in range(lengthB - lengthA):
                headB = headB.next

        # check for the intersection node
        while headA and headB:
            if headA == headB:
                return headA
            else:
                headA = headA.next
                headB = headB.next
        
        return None

    def getLength(self, head: ListNode) -> int:
        if not head:
            return 0
        return 1 + self.getLength(head.next)