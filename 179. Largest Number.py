from typing import List
from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))

        # compare
        def comparator(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0

        # Sort using the custom comparator
        nums.sort(key=cmp_to_key(comparator))

        result = ''.join(nums)
        return "0" if result[0] == "0" else result
