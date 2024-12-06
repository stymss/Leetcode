from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # Find the midddle node
        middle_node = self.findMiddle(head)

        # Create a new linked list
        headB = middle_node.next
        middle_node.next = None

        # perform logic
        left_sorted = self.sortList(head)
        right_sorted = self.sortList(headB)
        return self.mergeTwoSortedLists(left_sorted, right_sorted)

    def findMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        t, h = head, head.next
        while h and h.next:
            t, h = t.next, h.next.next

        return t

    def mergeTwoSortedLists(self, head: Optional[ListNode], headB: Optional[ListNode]) -> Optional[ListNode]:
        new_head = ListNode(-1)
        dummy = new_head

        while head and headB:
            if head.val <= headB.val:
                dummy.next = head
                head = head.next
            else:
                dummy.next = headB
                headB = headB.next
            dummy = dummy.next

        # check if any remaining
        dummy.next = head if head else headB
        
        return new_head.next
        