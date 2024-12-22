from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                temp = nums[k]
                nums[k] = nums[i]
                nums[i] = temp
                k+=1
        return k