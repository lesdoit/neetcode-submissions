class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        
        key_value_pairs = list(freq.items())
        sorted_key_value_pairs = sorted(key_value_pairs, key = lambda x: x[1], reverse=True)
        top_k_freq_pairs = sorted_key_value_pairs[:k]
        return [x[0] for x in top_k_freq_pairs]