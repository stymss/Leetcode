from typing import List

class Solution:
    # TC - O(n log n) (sorting) + O(n²) (loop + two-pointer search) ~~ O(n^2)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Initialise 
        output = set()

        # Sort the array to convert it into 2 sum problem
        nums.sort()

        # Business logic
        for i in range(len(nums)-2):
            j, k = i+1, len(nums)-1

            while j < k:
                summed_val = nums[i] + nums[j] + nums[k]
                if summed_val == 0:
                    output.add(tuple((nums[i], nums[j], nums[k])))

                    # Optimisations
                    while j < k and nums[j] == nums[j+1]:
                        j+=1
                    while j < k and nums[k] == nums[k-1]:
                        k-=1
                    j+=1
                    k-=1
                elif summed_val < 0:
                    j+=1
                else:
                    k-=1
        return list(output)