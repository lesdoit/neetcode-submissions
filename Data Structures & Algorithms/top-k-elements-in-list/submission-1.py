import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        
        key_value_pairs = list(freq.items())
        value_key_pairs = [(-v, k) for (k,v) in key_value_pairs]
        
        heapq.heapify(value_key_pairs) 
        ans = [] 
        
        for i in range(k):
            elem = heapq.heappop(value_key_pairs)
            ans.append(elem[1])
        return ans 