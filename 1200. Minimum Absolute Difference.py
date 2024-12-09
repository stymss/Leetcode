from typing import List

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # Since pairs which are sorted will have the Minimum Absolute Difference
        arr.sort()

        ans = []
        min_abs_diff = float('inf')
        
        for i in range(1, len(arr)):
            diff = arr[i] - arr[i - 1]
            if diff < min_abs_diff:
                min_abs_diff = diff

                # reset ans to hold just this pair
                ans = [[arr[i - 1], arr[i]]]
            elif diff == min_abs_diff:

                # append to ans if equal
                ans.append([arr[i - 1], arr[i]])

        return ans