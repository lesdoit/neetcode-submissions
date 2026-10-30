class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # dp(i, target): number of ways to get to target from array[i..n]
        # transitions:
        # dp(i, target) = (dp(i+1, target-nums)) + dp(i+1, target+nums)
        # base case: target == 0, return 1

        n = len(nums)
        memo = {}

        def dp(i, target):
            if i == n: 
                if target == 0 : return 1
                else: return 0
            if (i, target) in memo: return memo[(i, target)]
            ans = 0 
            ans += dp(i+1, target - nums[i])
            ans += dp(i+1, target + nums[i])
            memo[(i, target)] = ans 
            return ans
        
        return dp(0, target)