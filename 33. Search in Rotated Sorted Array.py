from typing import List

class Solution:
    # TC - O(logn)
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)-1
        while low <= high:
            mid = low + (high - low)//2
            if nums[mid] == target:
                return mid

            # when the array is sorted, rotated, one side from mid is sorted
            # search for the sorted side
            if nums[low] <= nums[mid]:
                # check if target lies in this sorted side
                if target >= nums[low] and target < nums[mid]:
                    high = mid-1
                else:
                    low = mid+1
            else:
                # this side is sorted so search here
                if target > nums[mid] and target <= nums[high]:
                    low = mid+1
                else:
                    high = mid-1
        return -1