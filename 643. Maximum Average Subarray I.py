from typing import List

class Solution:
    # can be solved using fixed size sliding window approach
    # TC - O(n)
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        # for first k size window
        k_wind_sum = sum(nums[:k])
        k_wind_avg = k_wind_sum / k
        max_avg = k_wind_avg

        # check for remaining nums
        for i in range(k, len(nums)):
            # Include the new element and adjust the window
            k_wind_sum = k_wind_sum + nums[i] - nums[i-k]
            k_wind_avg = k_wind_sum / k

            # Calculate average
            max_avg = max(max_avg, k_wind_avg)
        
        return max_avg
