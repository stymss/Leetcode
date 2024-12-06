import heapq
from typing import List

class Solution:
    # TC - O(nlogn)
    def sortArray(self, nums: List[int]) -> List[int]:
        heap = [] # min heap
        for num in nums:
            heapq.heappush(heap, num)

        sorted_nums = []
        while heap:
            sorted_nums.append(heapq.heappop(heap))

        return sorted_nums