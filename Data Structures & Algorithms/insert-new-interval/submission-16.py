import bisect 

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        def isOverlap(seg1, seg2):
            return max(seg1[0], seg2[0]) <= min(seg1[1], seg2[1])

        res = []

        for i in range(len(intervals)):
            if newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            elif isOverlap(newInterval, intervals[i]):
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1]),
                ]
            elif newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
        res.append(newInterval)
        return res            
            