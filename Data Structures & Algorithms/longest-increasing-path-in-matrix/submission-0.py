class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # dp(i, j) -> length of longest increasing path starting at (i,j)
        # transitions:
        # dp(i, j) -> 1 + dp(i + dx, j + dy) for dx, dy in dirs if 
        # grid[i+dx][j+dy] > grid[i][j]
        n, m = len(matrix), len(matrix[0])
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        
        def in_boundary(i, j):
            if i < 0 or j < 0 or i >= n or j >= m: return False
            return True

        memo = {}
        def dp(i, j):
            if (i, j) in memo: return memo[(i, j)]

            res = 1
            for dx, dy in dirs:
                if in_boundary(i + dx, j + dy) and matrix[i+dx][j+dy] > matrix[i][j]:
                    res = max(res, 1 + dp(i + dx, j + dy))
            
            memo[(i, j)] = res
            return res
        
        ans = 1
        for i in range(n):
            for j in range(m):
                ans = max(ans, dp(i, j))
        return ans
