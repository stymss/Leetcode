from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) < 2:
            return stones[0]

        max_heap = []

        # Put everything in max_heap
        for stone in stones:
            heapq.heappush(max_heap, -stone)

        # Logic
        while len(max_heap) > 1:
            # get the largest 2 stones
            stone_a = -1 * heapq.heappop(max_heap)
            stone_b = -1 * heapq.heappop(max_heap)

            if stone_b != stone_a:
                heapq.heappush(max_heap, -(stone_a - stone_b))
        
        return -heapq.heappop(max_heap) if max_heap else 0