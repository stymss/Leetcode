from typing import List, Optional
import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Pair:
    def __init__(self, list_val, list_node):
        self.list_val = list_val
        self.list_node = list_node

    def __lt__(self, other):
        return self.list_val < other.list_val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []  # Min heap

        # Add the first element of each list to the heap    
        for list_node in lists:
            if list_node:
                heapq.heappush(heap, Pair(list_node.val, list_node))

        # Create the final sorted list
        new_head = ListNode(-1)
        dummy_node = new_head

        while heap:
            # Get the smallest element
            pair = heapq.heappop(heap)

            # Attach this node to the result list
            dummy_node.next = pair.list_node
            dummy_node = dummy_node.next

            # Push the next element of this node's list to the heap
            if pair.list_node.next:
                heapq.heappush(heap, Pair(pair.list_node.next.val, pair.list_node.next))

        return new_head.next