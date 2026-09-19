"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        def isOverlap(segment1, segment2):
            if max(segment1.start, segment2.start) < min(segment1.end, segment2.end):
                return True
            return False
        
        intervals = sorted(intervals, key=lambda interval: (interval.start, interval.end))
        for i in range(len(intervals)-1):
            if isOverlap(intervals[i], intervals[i+1]):
                return False
        
        return True