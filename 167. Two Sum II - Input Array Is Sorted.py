from typing import List 

class Solution:
    # TC - O(n)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1

        while left <= right:
            summed_val = numbers[left] + numbers[right]
            if summed_val == target:
                return [left+1, right+1]
            elif summed_val < target:
                left += 1
            else:
                right -= 1
            