class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        def isOverlap(seg1, seg2):
            return max(seg1[0, seg2[0]]) <= min(seg1[1], seg2[1])
        
        if not intervals: return intervals

        intervals.sort()
        ans = intervals[:1]
        
        for i in range(1, len(intervals)):
            if ans[-1][1] >= intervals[i][0]: 
                ans[-1][1] = max(ans[-1][1], intervals[i][1])
            else:
                ans.append(intervals[i])
        
        return ans
        