import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, k - 1
        
        # use a heap to store the window. And, in each iteration, 
        # keep removing elements whose index is less than current value of l
        heap_w = [(-nums[i], i) for i in range(k)]
        heapq.heapify(heap_w)
        res = []
        
        while r < len(nums) - 1: 
            res.append(-heap_w[0][0])
            l += 1
            r += 1

            heapq.heappush(heap_w, (-nums[r], r))
            while heap_w[0][1] < l:
                heapq.heappop(heap_w)
        
        res.append(-heap_w[0][0])
        return res