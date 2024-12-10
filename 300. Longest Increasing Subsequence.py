from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # lis tracks LIS till the index i
        lis = [1]*len(nums)

        # Logic
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    lis[nums[i]] = max(lis[nums[i], lis[nums[j]+1]])

        return lis[len(nums)-1]
