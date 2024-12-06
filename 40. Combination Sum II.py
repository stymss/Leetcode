from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = set()
        self.genCombs(candidates, target, [], result, 0)
        return list(result)

    def genCombs(self, nums: List[int], target: int, temp: List[int], result: List[int], idx: int) -> None:
        if target == 0:
            result.add(tuple(temp[:]))
            return 
        
        if target < 0:
            return
        
        for i in range(idx, len(nums)):
            if i > idx and nums[i] == nums[idx]:
                continue
            temp.append(nums[i])
            self.genCombs(nums, target - nums[i], temp, result, i+1)
            temp.pop()
        