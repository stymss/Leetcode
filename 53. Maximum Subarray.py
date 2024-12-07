from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # If there is one element that provides the maximum sum
        max_sum = nums[0]
        current_sum = 0

        # Check every element
        for num in nums:

            # if current_sum < 0 then set it 0
            if current_sum < 0:
                current_sum = 0

            # add current element to the sum
            current_sum += num

            # check max_sum
            max_sum = max(max_sum, current_sum)
        
        return max_sum