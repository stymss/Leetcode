from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self.genCombs(candidates, target, [], result, 0)
        return result

    def genCombs(self, nums: List[int], target: int, temp: List[int], result: List[int], idx: int) -> None:
        if target == 0:
            result.append(temp[:])
            return 
        
        if target < 0:
            return
        
        for i in range(idx, len(nums)):
            temp.append(nums[i])
            self.genCombs(nums, target - nums[i], temp, result, i)
            temp.pop()
        