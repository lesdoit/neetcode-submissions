class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # use a min heap of size k
        # keep heap-pushing elements and popping if size exceeds 
        # k. The answer will be top of the heap at the end 
        min_heap = []
        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        return heapq.heappop(min_heap)
        