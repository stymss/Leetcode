from typing import List

class Solution:
    # TC - O(logn)
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ub, lb = self.ub(nums, target), self.lb(nums, target)

        # Check if element exists or not
        if lb != len(nums) and nums[lb] == target:
            return [lb, ub-1]
        else:
            return [-1, -1]

    # Lower bound - smallest idx where the element can be inserted
    def lb(self, nums: List[int], target: int) -> List[int]:
        low, high = 0, len(nums)-1
        ans = len(nums)
        while low <= high:
            mid = low + (high - low)//2
            if nums[mid] >= target:
                ans = mid
                high = mid-1
            else:
                low = mid+1
        return ans 

    # Upper bound - first idx of the element which is greater than the element can be inserted
    def ub(self, nums: List[int], target: int) -> List[int]:
        low, high = 0, len(nums)-1
        ans = len(nums)
        while low <= high:
            mid = low + (high - low)//2
            if nums[mid] > target:
                ans = mid
                high = mid-1
            else:
                low = mid+1
        return ans 