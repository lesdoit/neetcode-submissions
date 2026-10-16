class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # seems like an array partition problem again. 
        # will be of the dp form ends at i 
        # dp(i) -> can the string ending at i be partitioned in words 
        
        # transitions dp(i) -> if s[j:i] is in wordDict and dp(j), return true
        # where j goes from (i-20 to i-1) and can't fall outside of s from left 

        wordset = set(wordDict)
        n = len(s)
        memo = [-1] * n
        
        def dp(i):
            if memo[i] != -1: return memo[i]
            if i == -1: return 1

            for j in range(i, max(-1, i-20),  -1):
                # print(f"s[j:i+1]: {s[j:i+1]}")
                if s[j:i+1] in wordset and dp(j-1):
                    memo[i] = 1
                    return memo[i]
            
            memo[i] = 0
            return memo[i]
        
        return True if dp(n-1) == 1 else False