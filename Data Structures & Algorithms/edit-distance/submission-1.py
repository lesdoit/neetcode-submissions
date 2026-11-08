class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        # State defn: dp(i, j) -> min edit dis to convert word1[0..i] into word2[0..j]

        # transitions: 
        # 1. if j == 0, then return i for i deletions 
        # 2. if i == 0, then return j for j insertions 
        # ans = float('inf')
        # 3. if word1[i] == word2[j], then ans= min(ans,1 + dp(i-1, j-1)) - match 
        # 4. ans = min(ans, 1 + dp(i-1,j-1) - replace 
        # 5. ans = min(ans, 1 + dp(i-1, j)) - delete 
        # 6. ans = min(ans, 1 + dp(i, j-1)) - insert 
        # save state and return 
        memo = {}
        def dp(i, j):
            # base case 
            if j == -1: return i + 1
            if i == -1: return j + 1
            
            # cache lookup 
            if (i, j) in memo: return memo[(i, j)]

            # compute 
            ans = float('inf')
            print(f"i: {i}, j: {j}")
            if word1[i] == word2[j]:
                ans = min(ans, dp(i-1, j-1))     # match 
            else:
                ans = min(ans, 1 + dp(i-1, j-1)) # replace 
            ans = min(ans, 1 + dp(i-1, j))       # delete cur char in word1
            ans = min(ans, 1 + dp(i, j-1))       # insert a new char in word1
            memo[(i,j)] = ans 
            return ans 
        return dp(len(word1)-1, len(word2)-1)
        