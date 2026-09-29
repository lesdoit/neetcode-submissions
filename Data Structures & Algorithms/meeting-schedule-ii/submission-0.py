"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import collections 

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals: return 0
        mp = collections.defaultdict(int)
        for interval in intervals:
            mp[interval.start] += 1
            mp[interval.end] -= 1
        
        # print(f"mp: {mp}")
        ans = active = 0 
        for key, val in sorted(mp.items()):
            active += val
            ans = max(ans, active)
        
        return ans 
