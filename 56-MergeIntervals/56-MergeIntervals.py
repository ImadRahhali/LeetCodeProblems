# Last updated: 6/16/2025, 9:20:57 PM
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        intervals.sort()
        res = []
        curr_start = intervals[0][0]
        curr_end = intervals[0][1]
        for i in range(1,len(intervals)):
            if curr_end >= intervals[i][0]:
                curr_start = min(curr_start, intervals[i][0])
                curr_end = max(curr_end, intervals[i][1])

            else:
                res.append([curr_start, curr_end])
                curr_start = intervals[i][0]
                curr_end = intervals[i][1]
        res.append([curr_start, curr_end])
        return res
