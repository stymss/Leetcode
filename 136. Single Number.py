from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Using XOR
        xor = nums[0]
        for i in range(1, len(nums)):
            xor ^= nums[i]
        
        return xor