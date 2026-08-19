import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, k - 1
        heap = [(-nums[i], i) for i in range(k)]
        
        heapq.heapify(heap)
        res = []
        res.append(-heap[0][0])
        
        while r < len(nums) - 1:
            l += 1 
            r += 1 
            heapq.heappush(heap, (-nums[r], r))
            while heap[0][1] < l:
                heapq.heappop(heap)
            res.append(-heap[0][0])
        return res