class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def boundary_check(row, col, grid):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]): return False
            return True

        def dfs(grid, row, col):
            grid[row][col] = "0"
            directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
            for dx, dy in directions: 
                if boundary_check(row + dx, col + dy, grid) and \
                grid[row + dx][col + dy] == "1":
                    dfs(grid, row + dx, col + dy)
        
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    dfs(grid, i, j)
                    ans += 1
        
        return ans