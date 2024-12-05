from typing import List

class Solution:
    # TC - O(N^2)
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # Initialise 
        closest = float('inf')

        # Sort the array to convert it into 2 sum problem
        nums.sort()

        # Business logic
        for i in range(len(nums)-2):
            j, k = i+1, len(nums)-1

            while j < k:
                summed_val = nums[i] + nums[j] + nums[k]

                # Update the closest sum if current is closer to the target
                if abs(summed_val - target) < abs(closest - target):
                    closest = summed_val

                # Adjust pointers to approach the target
                if summed_val < target:
                    j += 1
                else:
                    k -= 1
        return closest