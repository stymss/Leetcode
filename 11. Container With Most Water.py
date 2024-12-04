from typing import List

class Solution:
    # O(n)
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        max_water = 0
        while left <= right:
            max_water = max(max_water, min(height[left], height[right])*(right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_water