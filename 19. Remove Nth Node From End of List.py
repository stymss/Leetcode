from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # get list length
        length = self.length(head)

        # check node to be deleted
        nodeidx_todel = length - n

        # logic
        count = 0
        cur = head
        prev = None 
        while count < nodeidx_todel:
            prev = cur 
            cur = cur.next 
            count += 1

        if not prev:
            return cur.next 
        else:
            prev.next = cur.next 
        
        return head

    def length(self, head: Optional[ListNode]) -> int:
        if not head:
            return 0
        
        return 1 + self.length(head.next)