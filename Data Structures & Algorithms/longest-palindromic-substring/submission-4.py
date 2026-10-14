class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 2D DP interval DP aka LR dp 
        
        n = len(s)
        memo = []
        for _ in range(n):
            row = [-1] * n
            memo.append(row)

        # returns if s[i:j] is palindrome (T/F) and returns the longest Pal in i..j
        def is_pal(i, j): 
            
            if memo[i][j] != -1: return memo[i][j]

            if i == j: 
                memo[i][j] = 1
                return memo[i][j]
            
            if i + 1 == j: 
                if s[i] == s[j]:
                    memo[i][j] = 1
                    return memo[i][j]
                else: 
                    memo[i][j] = 0
                    return memo[i][j]
            
            # print(f"i: {i}, j: {j}")

            if s[i] == s[j] and is_pal(i+1, j-1) == 1: 
                memo[i][j] = 1
                return memo[i][j]
            
            memo[i][j] = 0
            return memo[i][j]

        res = ""
        resLen = 0
        for i in range(n):
            for j in range(i, n):
                if is_pal(i, j):
                    if (j - i + 1) > resLen:
                        res = s[i:j+1]
                        resLen = (j - i + 1)
        return res 

        