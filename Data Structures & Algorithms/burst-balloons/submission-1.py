class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        # state: dp(l, r) -> for a segment L-R, what is the max cost to burst ballon 

        # transitions: 
        # idea: assume i goes from l to r inclusive. For every ith balloon, 
        # assume it is popped last. 
        # so cost of popping ith balloon last is -- 
        # (nums[l-1] * nums[i] * nums[r+1]) + dp(l, i-1) + dp(i+1, r)

        n = len(nums)
        new_nums = [1] + nums + [1]

        dp = [[0] * (n + 2) for _ in range(n + 2)]
        for l in range(n, 0, -1):
            for r in range(l, n + 1):
                for i in range(l, r + 1):
                    coins = new_nums[l - 1] * new_nums[i] * new_nums[r + 1]
                    coins += dp[l][i - 1] + dp[i + 1][r]
                    dp[l][r] = max(dp[l][r], coins)

        return dp[1][n]
        