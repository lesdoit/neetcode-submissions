import heapq
import collections 

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        q_idx_map = collections.defaultdict(list)
        for idx, elem in enumerate(queries): 
            q_idx_map[elem].append(idx)
        
        queries.sort()
        intervals.sort()

        ans = [-1] * len(queries)
        it = 0
        mheap = []
        for query in queries: 
            while it < len(intervals) and intervals[it][0] <= query: 
                heapq.heappush(mheap, (intervals[it][1] - intervals[it][0] + 1, 
                                            intervals[it][1]))
                it += 1
            
            while mheap and mheap[0][1] < query:
                heapq.heappop(mheap)

            if mheap: 
                idx = q_idx_map[query][0]
                q_idx_map[query] = q_idx_map[query][1:]
                ans[idx] = mheap[0][0]
        return ans