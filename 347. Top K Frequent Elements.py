from typing import List
import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Compute frequency
        freq_map = Counter(nums)

        # Create heap
        max_heap = [(-freq, num) for num, freq in freq_map.items()]
        heapq.heapify(max_heap)

        top_k = []
        for _ in range(k):
            top_k.append(heapq.heappop(max_heap)[1])

        return top_k