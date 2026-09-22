import bisect 

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        def isOverlap(seg1, seg2):
            return max(seg1[0], seg2[0]) <= min(seg1[1], seg2[1])

        # line sweep 
        i = 0 
        ans = [] 

        while i < len(intervals) and intervals[i][1] < newInterval[0]: 
            ans.append(intervals[i])
            i+=1
        
        while i < len(intervals) and isOverlap(intervals[i], newInterval): 
            newInterval = [
                min(intervals[i][0], newInterval[0]),
                max(intervals[i][1], newInterval[1])
                ]
            i += 1
        ans.append(newInterval)


        while i < len(intervals) and intervals[i][0] > newInterval[1]:
            ans.append(intervals[i])
            i += 1

        return ans

            
            