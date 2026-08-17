class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        total = 0
        
        for i in range(n):
            leftmax = 0 
            for j in range(i):
                leftmax = max(leftmax, height[j])
            
            rightmax = 0
            for k in range(i+1, n):
                rightmax = max(rightmax, height[k])
            
            if height[i] < leftmax and height[i] < rightmax: 
                total += (min(leftmax, rightmax) - height[i])

        return total