class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]

        def boundary_check(grid, r, c): 
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]): return False
            return True
        
        def dfs(grid, row, col): 
            size = 1
            grid[row][col] = 0
            for dr, dc in directions:
                if boundary_check(grid, row + dr, col + dc) and grid[row + dr][col + dc] == 1:
                    size += dfs(grid, row + dr, col + dc)
            return size
        
        ans = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1:
                    ans = max(ans, dfs(grid, row, col))
        return ans