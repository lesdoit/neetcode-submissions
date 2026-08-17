class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for index, num in enumerate(nums):
            for j in range(index):
                if nums[j] == num:
                    return True
        return False