class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        # state: dp(l, r) -> for a segment L-R, what is the max cost to burst ballon 

        # transitions: 
        # idea: assume i goes from l to r inclusive. For every ith balloon, 
        # assume it is popped last. 
        # so cost of popping ith balloon last is -- 
        # (nums[l-1] * nums[i] * nums[r+1]) + dp(l, i-1) + dp(i+1, r)

        nums = [1] + nums + [1]
        memo = {}
        def dp(l, r):
            # base 
            if l > r: return 0

            # cache check 
            if (l, r) in memo: return memo[(l, r)]
            
            # compute and persist in cache
            ans = float('-inf')
            for i in range(l, r + 1):
                cur = nums[l-1] * nums[i] * nums[r+1]
                cur += dp(l, i-1)
                cur += dp(i+1, r)
                ans = max(ans, cur)
            memo[(l, r)] = ans
            return ans
        return dp(1, len(nums) - 2)
        