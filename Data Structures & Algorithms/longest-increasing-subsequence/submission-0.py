class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # define state = dp(i) = length of LIS ending at i
        # define state transition: dp(i) = max(prev_ans, 1 + rec(j)) where nums[j] < nums[i] 
        # and j goes from 0 to i-1
        
        n = len(nums)
        memo = [[-1, -1] for _ in range(n)]
        
        def rec(i):
            if memo[i][0] != -1: 
                return memo[i][0]
            # print(f"i: {i}")
            # print(f"mem: {memo}")

            ans = 1
            memo[i][0] = 1
            memo[i][1] = i
            for j in range(0, i):
                if nums[j] < nums[i]:
                    at_j = 1 + rec(j)
                    if at_j > ans:
                        memo[i][0] = at_j
                        memo[i][1] = j
                        ans = at_j
            return memo[i][0]
        
        
        ans = 0
        for i in range(n):
            ans = max(ans, rec(i))
        return ans

