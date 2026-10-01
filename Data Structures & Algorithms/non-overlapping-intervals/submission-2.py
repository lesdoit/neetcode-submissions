class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        ans = 0 
        prevEnd = intervals[0][1]
        # keep the intervals with earliest end times 
        for start, end in intervals[1:]:
            if start >= prevEnd: 
                prevEnd = end
            else:
                ans += 1
        return ans