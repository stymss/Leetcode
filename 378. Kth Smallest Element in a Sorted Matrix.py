from typing import List
import heapq

class Solution:
    # O(n^2 log(k))
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = [] # max heap

        for row in matrix:
            for val in row:
                heapq.heappush(heap, -val)
                if len(heap) > k:
                    heapq.heappop(heap)
        
        return -heap[0]