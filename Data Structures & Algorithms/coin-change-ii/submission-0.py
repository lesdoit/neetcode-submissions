class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # state dp(i, remaining) - total ways to get to remaining by using coins[i..n]
        # transitions: 
        # dp(i, remaining) = take and advance + take and don't advance + 
        # don't take and advance 

        memo = {}
        n = len(coins)
        
        def dp(i, remaining):
            if i >= n: return 0
            if remaining == 0: return 1
            if remaining < 0: return 0

            if (i, remaining) in memo: return memo[(i, remaining)]

            ans = 0
            if remaining == coins[i]:
                ans += 1                        # take_stay. SKIP take_adv 
            else:
                # ans += dp(i + 1, remaining - coins[i])      # take_adv
                ans += dp(i, remaining - coins[i])          # take_stay
                ans += dp(i + 1, remaining)                 # skip_adv
            memo[(i, remaining)] = ans
            return memo[(i, remaining)]
        
        return dp(0, amount)

            