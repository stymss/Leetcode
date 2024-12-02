from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        k = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                temp = nums[k]
                nums[k] = nums[i]
                nums[i] = nums[k]
                k+=1
        
        for i in range(k, len(nums)):
            nums[i] = 0