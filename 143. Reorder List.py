from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find middle node and create a new list using it
        middle_node = self.findMiddle(head)
        head2 = middle_node.next
        middle_node.next = None 

        # reverse second LL
        h2 = self.reverseList(head2)

        # reorder list
        cur1, cur2 = head, h2
        while cur1 and cur2:
            # store next of cur1 for rejoining
            next1, next2 = cur1.next, cur2.next

            cur1.next = cur2
            cur2.next = next1 
            cur1 = next1 
            cur2 = next2

        return head

    def findMiddle(self, head: Optional[ListNode]) -> ListNode:
        t, h = head, head.next
        while h and h.next:
            t, h = t.next, h.next.next 
        return t 
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        next, prev = None, None
        cur = head
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev