from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result_intervals = []

        # Traverse through all the intervals
        for interval in intervals:
            # if interval is less than newInterval, add interval to the output
            if interval[1] < newInterval[0]:
                result_intervals.append(interval)
            # if new interval is not coinciding with any other interval
            elif newInterval[1] < interval[0]:
                result_intervals.append(newInterval)
                newInterval = interval # set this interval to new_interval for further comparison
            # when merge is required
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
            
        # At this point we have processed everything and are left with a final interval
        result_intervals.append(newInterval)

        return result_intervals
