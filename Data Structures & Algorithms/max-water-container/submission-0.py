class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # area = (shorter height) * width 
        area = 0
        i, j = 0, len(heights) - 1
        while i < j:
            curr_area = (min(heights[i], heights[j]) * (j - i)) 
            area = max(area, curr_area) 
            if heights[i] < heights[j]: 
                i += 1
            else:
                j-= 1
        
        return area