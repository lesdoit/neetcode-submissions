class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # dp(j, k) -> returns true if there is a 
        # interleaving possible with values s1[0..j] and s2[0..k] resulting in s3[0.. j+k+1]

        # transitions: 
        # dp(j, k): 
        # 1. if s1[j] == s3[j+k+1] and dp(j-1, k): return true 
        # 2. if s2[k] == s3[j+k+1] and dp(j, k-1): return true 
        # 3. return false otherwise 
        
        s1len = len(s1)
        s2len = len(s2)
        s3len = len(s3)
        if s3len != s1len + s2len: return False

        memo = {}

        def dp(j, k):
            # base case 
            if j == -1 and k == -1: 
                return True
            
            # cache lookup 
            if (j, k) in memo: return memo[(j, k)]

            # compute 
            if j > -1 and s1[j] == s3[j+k+1] and dp(j - 1, k):  
                memo[(j, k)] = True
            elif k > -1 and s2[k] == s3[j+k+1] and dp(j, k - 1): 
                memo[(j, k)] = True
            else: 
                memo[(j, k)] = False
            return memo[(j, k)]
        
        return dp(s1len - 1, s2len - 1)