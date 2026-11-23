class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        all_xor = 0
        for i in range(n+1):
            all_xor ^= i
        for num in nums:
            all_xor ^= num
        return all_xor