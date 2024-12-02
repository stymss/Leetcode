from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # We can use tortoise-hare algorithm
    # TC - O(n)
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        t, h = head, head
        while h and h.next:
            t, h = t.next, h.next.next
            if t == h:
                return True 
        return False