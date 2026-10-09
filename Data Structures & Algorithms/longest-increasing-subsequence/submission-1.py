class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # define state = dp(i) = length of LIS ending at i
        # define state transition: dp(i) = max(prev_ans, 1 + rec(j)) where nums[j] < nums[i] 
        # and j goes from 0 to i-1
        
        n = len(nums)
        memo = [-1 for _ in range(n)]
        
        def rec(i):
            if memo[i] != -1: 
                return memo[i]
            
            ans = memo[i] = 1 
            for j in range(0, i):
                if nums[j] < nums[i]:
                    ans = max(ans, 1 + rec(j))
            memo[i] = ans
            return ans
        
        
        ans = 0
        for i in range(n):
            ans = max(ans, rec(i))
        return ans

