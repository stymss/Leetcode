from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, head: Optional[ListNode], headB: Optional[ListNode]) -> Optional[ListNode]:
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
        