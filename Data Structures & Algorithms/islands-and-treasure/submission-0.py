import collections

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        def boundary_check(r, c):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
                return False
            return True
        
        q = collections.deque()
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 0:
                    q.append((r, c, 0))
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        while q:
            r, c, dist = q.popleft()
            for dr, dc in directions: 
                if boundary_check(r + dr, c + dc) and \
                    grid[r + dr][c + dc] != -1: 
                    if grid[r + dr][c + dc] > dist + 1:
                        grid[r + dr][c + dc] = dist + 1
                        q.append((r + dr, c + dc, dist + 1))
        


