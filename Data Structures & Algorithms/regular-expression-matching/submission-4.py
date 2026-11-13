class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # dp(i, j) -> does s[i..n] match with p[j..m] where n, m = len(s), len(p)
        # transitions: 
        # dp(i, j) = 
        #   if s[i] == p[j] or p[j] == '.': 
        #      if dp(i+1, j+1): return true 
        #   if p[j] == '*':
        #      if dp(i+1, j) or dp(i+1, j+1) or dp(i, j+1): return true
        #   return false 

        n, m = len(s), len(p)
        memo = {}
        
        def dp(i, j):
            # base case
            if i == n and j == m: return True
            if j == m and i < n: return False

            # cache lookup
            if (i, j) in memo: return memo[(i,j)]

            # compute and save 
            ans = False
            if i < n and j < m and (s[i] == p[j] or p[j] == '.') and dp(i+1, j+1):
                ans = True
            elif j < m - 1 and p[j+1] == '*': 
                if dp(i, j+2):                 # match zero times
                    ans = True
                elif i < n and j < m and (s[i] == p[j] or p[j] == '.') and dp(i+1, j+2):
                    ans = True
                elif i < n and j < m and (s[i] == p[j] or p[j] == '.') and dp(i+1, j):
                    ans = True
            
            memo[(i,j)] = ans 
            return ans
        
        return dp(0, 0)