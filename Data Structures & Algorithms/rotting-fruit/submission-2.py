import collections

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        def boundary_check(r, c): 
            if r<0 or r>=len(grid) or c<0 or c>=len(grid[0]): 
                return False
            return True

        q = collections.deque()
        fresh_fruit = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 2:
                    q.append((r, c, 0))
                elif grid[r][c] == 1:
                    fresh_fruit += 1
        
        if not fresh_fruit: return 0
        
        ans = -1
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while q: 
            r, c, mins = q.popleft()
            for dr, dc in dirs: 
                if boundary_check(r+dr, c+dc) and grid[r+dr][c+dc] == 1:
                    ans = max(ans, mins + 1)
                    grid[r+dr][c+dc] = 2
                    fresh_fruit -= 1
                    q.append((r+dr, c+dc, mins + 1))
        
        return ans if not fresh_fruit else -1

