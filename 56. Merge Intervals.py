from typing import List

class Solution:
    # TC - O(nlogn)
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort intervals on the basis of start time TC - O(nlogn)
        sorted_intervals = sorted(intervals, key = lambda x:x[0])

        # TC - O(n)
        output = [sorted_intervals[0]]
        for i in range(1, len(sorted_intervals)):
            old_interval = output[-1]
            if old_interval[1] >= sorted_intervals[i][0]:
                # these intervals can be merged
                old_interval[1] = max(old_interval[1], sorted_intervals[i][1])
            else:
                # cannot be merged, so append to output
                output.append(sorted_intervals[i])
        return output