from typing import List

class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        # for this we can check if each element can qualify as a peak and if yes, than what is the longest mountain this peak creates
        longest = 0

        for i in range(1, len(arr)-1):
            # If the mountain condition satisifes
            if arr[i-1] < arr[i] > arr[i+1]:

                # Expand to the left
                l = i - 1
                while l > 0 and arr[l] > arr[l - 1]:
                    l -= 1
                
                # Expand to the right
                r = i + 1
                while r < len(arr) - 1 and arr[r] > arr[r + 1]:
                    r += 1
                
                longest = max(longest, r-l+1)
        
        return longest
    