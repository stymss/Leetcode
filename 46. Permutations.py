from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        self.generate(nums, permutations, [], set())
        return permutations

    def generate(self, nums, permutations, temp, seen):
        if len(temp) == len(nums):
            permutations.append(temp[:])
            return
        
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen.add(nums[i])
                temp.append(nums[i])
                self.generate(nums, permutations, temp, seen)
                temp.pop()
                seen.remove(nums[i])