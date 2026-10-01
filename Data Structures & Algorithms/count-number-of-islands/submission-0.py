class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def boundary_check(row, col, grid):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]): return False
            return True

        def dfs(grid, visited, row, col):
            visited[row][col] = True
            directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
            for dx, dy in directions: 
                if boundary_check(row + dx, col + dy, grid) and \
                not visited[row + dx][col + dy] and \
                grid[row + dx][col + dy] == "1":
                    dfs(grid, visited, row + dx, col + dy)

        visited = []
        for i in range(len(grid)):
            visitedRow = [False] * len(grid[0])
            visited.append(visitedRow)
        
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if not visited[i][j] and grid[i][j] == "1":
                    dfs(grid, visited, i, j)
                    ans += 1
        
        return ans