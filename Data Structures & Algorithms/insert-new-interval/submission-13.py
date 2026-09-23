import bisect 

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        if not intervals: return [newInterval]

        ip = bisect.bisect_left(intervals, newInterval)
        
        ans = intervals[:ip]
        
        if ans and ans[-1][1] >= newInterval[0]:
            ans[-1][0] = min(ans[-1][0], newInterval[0])
            ans[-1][1] = max(ans[-1][1], newInterval[1])
        else: 
            ans.append(newInterval)
        
        i = ip 
        while i < len(intervals): 
            if ans and ans[-1][1] >= intervals[i][0]: 
                ans[-1][0] = min(ans[-1][0], intervals[i][0])
                ans[-1][1] = max(ans[-1][1], intervals[i][1])
            else: 
                ans.append(intervals[i])
            i += 1 
        return ans
            
            