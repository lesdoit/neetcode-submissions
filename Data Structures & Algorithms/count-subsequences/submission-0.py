class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # dp(i, j) -> how many number of distinct 
        # subsequences of s[0..i] are equal to t[0..j] ? 
        # transitions: ans = 0 
        # if s[i] == t[j]: ans += dp(i-1, j-1)
        # ans += dp(i-1, j)

        memo = {}
        def dp(i, j):
            # base case
            if j == -1: return 1
            if j != -1 and i == -1: return 0
            if (i, j) in memo: return memo[(i,j)]
            
            ans = 0
            if s[i] == t[j]: 
                ans += dp(i-1, j-1)
            ans += dp(i-1, j)
            memo[(i,j)] = ans 
            return ans
        
        return dp(len(s)-1, len(t)-1)

