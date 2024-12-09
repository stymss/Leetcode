from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Approach - 1 -> Using set
        # return True if len(nums) != len(set(nums)) else False

        # Approach - 2 -> Using Sorting
        # Base Case
        if len(nums) < 2:
            return False
            
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == nums[i-1]:
                # we have encountered duplicates, return true directly
                return True
        return False