from typing import List

class Solution:
    # Brute force (O(n^2))
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return [-1, -1]

    # Optimised (O(n))
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for idx, val in enumerate(nums):
            search_ele = target - val
            if search_ele in dict:
                return [idx, dict[search_ele]]
            else:
                dict[val] = idx
        return [-1, -1]