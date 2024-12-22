from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                k += 1
                temp = nums[i]
                nums[k], nums[i] = nums[i], temp
            
        return k+1