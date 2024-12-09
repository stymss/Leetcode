from typing import List

class Solution:
    # TC - O(nlogn)
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            result.append(num ** 2)

        return sorted(result)
    
class Solution:
    # TC - O(n)
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [0]*len(nums)
        i, j, k = 0, len(nums)-1, len(nums)-1

        # Check till we have exhausted the nums array
        while i <= j:
            i_sq, j_sq = nums[i]**2, nums[j]**2
            if j_sq >= i_sq:
                result[k] = j_sq
                j-=1
            else:
                result[k] = i_sq
                i+=1
            k -= 1
        
        return result