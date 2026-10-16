class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # this is like an instance of 0/inf knapsack problem 
        # it is possible to solve this using 2D dp or 1D dp 
        
        # Let's now try with 2D dp 
        # dp(i, remaining) -> return min num of coins to 
        # get to remaining amt from ith index to (n-1)th index 

        # transitions -
        # dp(i, remaining) = min(1 + dp(i, remaining - coins[i]), dp(i+1, remaining))
        n = len(coins)
        memo = []
        for _ in range(n):
            row = [-1] * 10001
            memo.append(row)

        def dp(i, remaining):
            # base case
            if i > n - 1 or remaining < 0: 
                return int(1e9)     # penalty for never considering this option
            
            if remaining == 0: 
                memo[i][remaining] = 0
                return memo[i][remaining]

            if memo[i][remaining] != -1: return memo[i][remaining]

            if coins[i] == remaining:
                memo[i][remaining] = 1
                return memo[i][remaining]
            
            memo[i][remaining] = min(1 + dp(i, remaining - coins[i]), dp(i+1, remaining))
            return memo[i][remaining]
        
        res = dp(0, amount)
        return res if res != int(1e9) else -1
        
        
