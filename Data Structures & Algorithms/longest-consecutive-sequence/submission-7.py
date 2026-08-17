class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: 
            return 0
        if len(nums) == 1:
            return 1

        nums.sort()
        result, streak = 1, 1
        i, j = 0, 1
        y = [1, 1, 1, 1, 2, 2, 2, 4, 6, 7, 8, 9]
        
        while i < len(nums) and j < len(nums):
            if nums[j] == nums[i]: 
                j += 1
            elif nums[j] == nums[i] + 1:
                streak += 1 
                i = j
                j += 1
                result = max(result, streak)
            else:
                streak = 1
                i = j
                j += 1
        return result

