from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        dict = {}

        # sort the nums
        sorted_nums = sorted(nums)

        # check for every element
        for idx, num in enumerate(sorted_nums):
            if num not in dict:
                dict[num] = idx
        
        ans = []
        for num in nums:
            ans.append(dict[num])
        return ans