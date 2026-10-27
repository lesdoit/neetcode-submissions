class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # knapsack - most likely 
        
        # observe that to get sum(subset1) == sum(subset2), a necesary condition 
        # would be to make sure that both subsets sum upto exact = total_sum/2

        # solve 2 knapsacks with exact sum and 
        # if there exists two or more solutions, return true

        target = sum(nums)
        if target%2 != 0: return False

        target //= 2
        subset_cnt = 0
        n = len(nums)
        
        memo = []
        for _ in range(n):
            r = [-1] * (target + 1)
            memo.append(r)
        
        # dp(i, target) -> is it possible to achieve this target starting at 
        # index i and using only the next elements (picking each element at most once)
        def dp(i, target):
            if target < 0: return 0
            if i == n and target == 0: return 1
            if i == n and target != 0: return 0
            
            if memo[i][target] != -1: return memo[i][target]
            
            if target == 0: 
                memo[i][target] = 1
                return memo[i][target]
            
            possible = 0
            possible += dp(i + 1, target)
            possible += dp(i + 1, target - nums[i])
            if possible > 0: 
                memo[i][target] = 1
            else: 
                memo[i][target] = 0
            return memo[i][target]
        
        # subset_cnt = 0
        # for i in range(n):
        #     if dp(i, target) == 1:
        #         subset_cnt += 1
        
        # print(f"memo: {memo}")        
        
        return True if dp(0, target) == 1 else False
        
        
