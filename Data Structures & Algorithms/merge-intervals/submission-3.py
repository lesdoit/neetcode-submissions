import collections

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        mp = collections.defaultdict(int)
        for interval in intervals:
            mp[interval[0]] += 1
            mp[interval[1]] -= 1
        
        sorted_mp = dict(sorted(mp.items()))
        ans = []
        have = 0
        cur_interval = []
        
        for key, val in sorted_mp.items():
            if not cur_interval:
                cur_interval.append(key)
            have += val
            if have == 0:
                cur_interval.append(key) 
                ans.append(cur_interval)
                cur_interval = []
        return ans
        