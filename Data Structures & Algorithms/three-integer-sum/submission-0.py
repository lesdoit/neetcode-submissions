class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = set()
        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range (j+1, n):
                    if nums[i] + nums[j] + nums[k] == 0: 
                        ans.add(tuple(sorted([nums[i], nums[j], nums[k]])))
        ans = [[a, b, c] for (a, b, c) in ans]
        return ans