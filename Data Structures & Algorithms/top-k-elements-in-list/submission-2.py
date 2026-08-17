import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(len(nums) + 1)]
        freq = defaultdict(int)
        
        for n in nums: 
            freq[n] += 1
        
        for key, v in freq.items():
            buckets[v].append(key)
        
        print(buckets)

        ans = []
        for i in range(len(nums), 0, -1): 
            bucket = buckets[i]
            for num in bucket: 
                ans.append(num)
                if len(ans) == k: 
                    return ans
