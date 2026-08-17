class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        
        prefix = [0] * n
        for i in range(n):
            if i > 0:
                prefix[i] = max(prefix[i-1], height[i])
            else:
                prefix[i] = height[i]
        
        suffix = [0] * n
        for i in range(n-1, -1, -1):
            if i == n-1:
                suffix[i] = height[i]
            else:
                suffix[i] = max(suffix[i+1], height[i])
        
        total = 0
        for i in range(n):
            leftmax = prefix[i]
            rightmax = suffix[i]
            if height[i] < leftmax and height[i] < rightmax:
                total += (min(leftmax, rightmax) - height[i])

        return total