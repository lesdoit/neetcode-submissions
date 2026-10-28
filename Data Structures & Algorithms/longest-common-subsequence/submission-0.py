class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        # This is a form 3 - multi sec dp
        # dp(i, j) for a string text1[i..m] and text2[j..n], what is the length of the 
        # longest common subsequence 
        # transitions: max(1 + dp(i+1, j+1) if text1[i] == text2[j], dp(i+1, j), 
        # dp(i, j+1))
        m, n = len(text1), len(text2)
        memo = [[-1]*n for _ in range(m)]

        def dp(i, j):
            # base case 
            if i >= m or j >= n: return 0

            if memo[i][j] != -1: return memo[i][j]

            ans = 0 
            ans = max(ans, dp(i+1, j))
            ans = max(ans, dp(i, j+1))
            if text1[i] == text2[j]:
                ans = max(ans, 1 + dp(i+1, j+1))
            
            memo[i][j] = ans 
            return ans
        
        return dp(0, 0)