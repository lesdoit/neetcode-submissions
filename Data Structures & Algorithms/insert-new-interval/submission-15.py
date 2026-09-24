import bisect 

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        if not intervals: return [newInterval]

        # Find first interval ending >= newInterval[0]
        left = bisect.bisect_left(intervals, newInterval[0], key=lambda x: x[1])
        # Find first interval starting > newInterval[1]
        right = bisect.bisect_right(intervals, newInterval[1], key=lambda x: x[0])

        # Overlapping slice is intervals[left:right]
        if left < right:
            newInterval[0] = min(newInterval[0], intervals[left][0])
            newInterval[1] = max(newInterval[1], intervals[right - 1][1])

        return intervals[:left] + [newInterval] + intervals[right:]
            
            