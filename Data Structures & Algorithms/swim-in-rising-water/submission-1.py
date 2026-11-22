class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visited = set()
        pq = [(grid[0][0], 0, 0)]       # max heigh seen so far, r, c
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        while pq:
            h, r, c = heapq.heappop(pq)
            if r == N-1 and c == N-1: return h
            if (r, c) in visited: continue
            visited.add((r, c))

            for dr, dc in directions: 
                if min(r + dr, c + dc) < 0 or \
                    max(r + dr, c + dc) == N: 
                    continue
                heapq.heappush(pq, (max(grid[r + dr][c + dc], h), r + dr, c + dc))
        
        return -1