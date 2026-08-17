class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        if n == 1:
            return heights[0]
        next_smallest_idx = [n] * n 
        prev_smallest_idx = [-1] * n 

        # use monotonic increasing stack to populate next smallest idx
        mi_nxt_stack = collections.deque()
        for i, elem in enumerate(heights):
            while mi_nxt_stack and elem < mi_nxt_stack[-1][0]:
                content, idx = mi_nxt_stack.pop()
                next_smallest_idx[idx] = i
            mi_nxt_stack.append((elem, i))
        
        # use monotonic increasing stack to populate prev smallest idx 
        mi_prev_stack = collections.deque()
        for i in range(n - 1, -1, -1):
            while mi_prev_stack and heights[i] < mi_prev_stack[-1][0]:
                content, idx = mi_prev_stack.pop()
                prev_smallest_idx[idx] = i
            mi_prev_stack.append((heights[i], i))
        
        print(f"next smaller - {next_smallest_idx}") 
        print(f"prev_smaller - {prev_smallest_idx}")

        ans = 0
        for i, height in enumerate(heights):
            cur = height * (next_smallest_idx[i] - prev_smallest_idx[i] - 1)
            ans = max(ans, cur)
        
        return ans
