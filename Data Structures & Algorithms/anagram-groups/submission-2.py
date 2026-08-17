from collections import defaultdict
from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_string_map = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            freq_string_map[tuple(count)].append(s)
        
        return list(freq_string_map.values())
        
