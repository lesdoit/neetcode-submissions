class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # DP form 2 - Ends at i 
        # dp(i, j) -> how many ways to get to this cell 
        # transitions -> 
        # dp(i, j) = dp(i-1, j) + dp(i, j-1)
        
        prevRow = [0] * (n+1)
        curRow = [0] * (n+1)
        curRow[0] = 1
        if m == 1 and n == 1: return 1

        for i in range(m):
            for j in range(1, n+1):
                curRow[j] = curRow[j-1] + prevRow[j]
            prevRow = curRow
            curRow = [0] * (n+1)

        return prevRow[n]