class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = [-1] * n
        
        def rec(floor):
            if floor >= n: 
                return 0
            
            if memo[floor] != -1:
                return memo[floor]
            
            memo[floor] = min(cost[floor] + rec(floor+1), cost[floor] + rec(floor+2))
            return memo[floor]
        
        rec(0)
        
        return min(memo[0], memo[1])