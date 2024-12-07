from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        # If 1 home, rob it
        if len(nums) == 1:
            return nums[0]
        
        # If 2 homes, rob the max home
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        dp = [0]*len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        # Apply the same logic for other houses
        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])

        # Return the final ans
        return dp[len(nums)-1]