class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # let's try with knapsack style dp 
        # dp(i, can_buy): max profit for array ending at i assuming you can/not buy 
        # today. 

        # transitions 
        # if you can buy, then two options- buy today and advance by 1 or do not buy
        # and advance by 1 
        # if you can't buy then two options- sell today and advance by 2 or don't sell
        # and advance by 1
        memo = {}
        n = len(prices)
        def dp(i, can_buy):
            if i >= n: return 0
            if (i, can_buy) in memo: return memo[(i, can_buy)]

            ans = float('-inf')
            if can_buy: 
                ans = max(ans, -prices[i] + dp(i+1, False))
                ans = max(ans, dp(i+1, can_buy))
            else:
                ans = max(ans, prices[i] + dp(i+2, True))
                ans = max(ans, dp(i+1, can_buy))
            
            memo[(i, can_buy)] = ans
            return ans

        return dp(0, True)