from typing import List

class Solution:
    # # Brute Force TC - O(n) SC - O(n)
    # def findDuplicate(self, nums: List[int]) -> int:
    #     seen = set()
    #     for num in nums:
    #         if num in seen:
    #             return num
    #         else:
    #             seen.add(num)

    # Brute Force 2 TC - O(nlogn) + O(n)
    # def findDuplicate(self, nums: List[int]) -> int:
    #     nums.sort()
    #     for i in range(len(nums)):
    #         if i+1 != nums[i]:
    #             return nums[i]

    # Optimised
    # O(n)
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            cur_idx_val = abs(nums[i])
            
            if nums[cur_idx_val - 1] < 0:
                return cur_idx_val
            else:
                nums[cur_idx_val - 1] *= -1
                