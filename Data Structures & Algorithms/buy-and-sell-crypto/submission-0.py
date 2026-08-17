class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = float('inf')
        profit = 0

        for i, num in enumerate(prices):
            lowest = min(lowest, num)
            profit = max(profit, num - lowest)
        
        return profit