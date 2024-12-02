from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # TC - O(n)
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Find middle node 
        middle_node = self.findMiddle(head)

        # create a second linked list from the middle node
        new_head = middle_node.next 
        middle_node.next = None 

        # reverse this new ll
        reversed_head = self.reverse(new_head)

        # Check for palindrome
        while head and reversed_head:
            if head.val != reversed_head.val:
                return False 
            if head:
                head = head.next
            if reversed_head:
                reversed_head = reversed_head.next
        return True
    
    # TC - O(n)
    def findMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        t, h = head, head.next
        while h and h.next:
            t, h = t.next, h.next.next
            
        return t
    
    # TC - O(n)
    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur, next, prev = head, None, None
        while cur:
            next = cur.next 
            cur.next = prev 
            prev = cur 
            cur = next 
        return prev