from typing import List

class Solution:
    # TC - O(nlogn)
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            result.append(num ** 2)

        return sorted(result)
    