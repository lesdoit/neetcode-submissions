class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # DP form 2 - Ends at i 
        # dp(i, j) -> how many ways to get to this cell 
        # transitions -> 
        # dp(i, j) = dp(i-1, j) + dp(i, j-1)
        memo = [[-1] * n for _ in range(m)]
        if m == 1 and n == 1: return 1

        def dp(i, j):
            if i < 0 or i >= m or j < 0 or j>=n:
                return 0
            if i + j == 1: return 1
            
            if memo[i][j] != -1: return memo[i][j]
            memo[i][j] = dp(i-1, j) + dp(i, j-1)
            return memo[i][j]

        return dp(m-1, n-1)

        