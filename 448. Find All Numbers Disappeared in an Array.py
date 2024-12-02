from typing import List

class Solution:
    # TC - O(n)
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Convert to set for removing duplicates
        nums_set = set(nums)

        # Check for missing
        missing = []
        for i in range(0, len(nums)):
            if i+1 not in nums_set:
                missing.append(i+1)
        return missing
    