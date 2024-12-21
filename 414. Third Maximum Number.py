from typing import List

import heapq

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nset = set(nums)
        heap = []

        for num in nset:
            heapq.heappush(heap, num)
            if len(heap) > 3:
                heapq.heappop(heap)
        
        if len(heap) == 2:
            return heap[-1]
        else:
            return heap[0]