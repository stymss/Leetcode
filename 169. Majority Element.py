from typing import List

class Solution:
    # Boyer Moore's Voting Algorithm
    def majorityElement(self, nums: List[int]) -> int:
        candidate, votes = -1, 0
        for num in nums:
            if votes == 0:
                candidate = num
                votes = 1
            else:
                if num == candidate:
                    votes += 1
                else:
                    votes -= 1
        
        # Check if the candidate is the majority element
        count = 0
        for i in range(len(nums)):
            if nums[i] == candidate:
                count += 1

        return candidate if count >= len(nums)//2 else -1