from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # check for the first and last element
        if len(nums) < 2 or nums[0] > nums[1]:
            return 0

        if nums[-1] > nums[-2]:
            return len(nums)-1

        low, high = 1, len(nums)-2
        while low <= high:
            mid = low + (high - low)//2
            # if it is the peak
            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid
            else:
                # increasing slope
                if nums[mid] < nums[mid+1]:
                    low = mid+1
                else:
                    high = mid-1
        return -1