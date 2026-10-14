class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # this is like an instance of 0/inf knapsack problem 
        # it is possible to solve this using 2D dp or 1D dp 
        
        # first try using 1D dp: 
        # state definition: dp(remaining) -> min number of coins reqd to get to rem
        # -1 - not computed 
        # int(1e9) - not possible 
        
        n = len(coins)
        memo = [-1] * (amount + 1)
        
        def dp(remaining):
            if remaining < 0: return int(1e9)
            if memo[remaining] != -1: return memo[remaining]
            
            if remaining == 0: 
                memo[remaining] = 0
                return memo[remaining]
            
            ans = int(1e9)
            for coin in coins:
                ans = min(ans, 1 + dp(remaining - coin))

            memo[remaining] = ans
            return memo[remaining]
        
        res = dp(amount)
        if res == int(1e9): return -1
        else: return res
