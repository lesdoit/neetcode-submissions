class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        s = set(nums)
        for i in range(len(nums) + 1):
            if i not in s: return i
        

        # n = len(nums)
        # mid = n//2
        # ans = 0
        
        # for num in nums:
        #     if num <= mid:
        #         ans ^= num
        #     else:                       # num > mid:
        #         ans ^= (num - mid)
        
        # return ans
