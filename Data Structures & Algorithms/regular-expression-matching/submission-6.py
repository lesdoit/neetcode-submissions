class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # State:
        #   dp(i, j) -> whether suffix s[i:] matches pattern suffix p[j:]
        #
        # Base Cases:
        #   i == n and j == m -> True
        #   j == m and i < n  -> False
        #
        # Transitions (let match = i < n and (s[i] == p[j] or p[j] == '.')):
        #   1. Direct single-char match:
        #        match and dp(i + 1, j + 1)
        #   2. Wildcard '*' lookahead (if j + 1 < m and p[j + 1] == '*'):
        #        dp(i, j + 2)                 # match 0 times (skip 'x*')
        #        or (match and dp(i + 1, j + 2)) # match 1 time
        #        or (match and dp(i + 1, j))     # match multiple times (keep 'x*')

        n, m = len(s), len(p)
        memo = {}
        
        def dp(i, j):
            # base case
            if i == n and j == m: return True
            if j == m and i < n: return False

            # cache lookup
            if (i, j) in memo: return memo[(i,j)]

            ans = False
            # direct character match or dot character 
            ans = (i < n and (s[i] == p[j] or p[j] == '.') and dp(i+1, j+1))
            
            if j < m - 1 and p[j+1] == '*': 
                ans = ans or dp(i, j+2)                 # match zero times
                ans = ans or (i < n and j < m and (s[i] == p[j] or p[j] == '.') and dp(i+1, j+2)) # match once 
                ans = ans or (i < n and j < m and (s[i] == p[j] or p[j] == '.') and dp(i+1, j))   # match multiple
            
            memo[(i,j)] = ans 
            return ans
        
        return dp(0, 0)