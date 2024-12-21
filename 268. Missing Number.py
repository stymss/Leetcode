from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Sort the nums so that val matches the idx
        nums.sort()

        # Check for the missing number
        for idx, val in enumerate(nums):
            if idx != val:
                return idx
        return len(nums) # If no numbers are missing, return the next number of the sequence
    
    def missingNumber(self, nums: List[int]) -> int:
        ns = set(nums)
        for i in range(len(nums)+1):
            if i not in ns:
                return i