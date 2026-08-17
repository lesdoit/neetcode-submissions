from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_map = defaultdict(list)
        for s in strs:
            sorted_s = ''.join(sorted(s))
            sorted_map[sorted_s].append(s)
        
        return list(sorted_map.values())
        
