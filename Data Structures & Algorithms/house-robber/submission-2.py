class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1: return nums[0] 

        n = len(nums)
        memo = [-1] * n
        
        def rec(level):
            if level == n or level == n + 1: return 0
            if memo[level] != -1: return memo[level]

            take = nums[level] + rec(level + 2)
            donttake = rec(level + 1)
            memo[level] = max(take, donttake)
            return memo[level]
        
        rec(0)
        return max(memo[0], memo[1])
