class Solution:
    def twoSum(self, nums, start, end, target): 
        print("in twosum")
        ans = []
        while start < end: 
            if nums[start] + nums[end] == target: 
                ans.append([nums[start], nums[end]])
                start += 1  # or end -= 1 
            elif nums[start] + nums[end] < target: 
                start += 1
            else: 
                end -= 1
        print(ans)
        return ans

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        n = len(nums)
        nums = sorted(nums)
        # fix a number and run two sum on the right side of the
        # list 
        for i in range(n):
            complement = 0 - nums[i]
            couples = self.twoSum(nums, i+1, n - 1, complement)
            for couple in couples: 
                result.add(tuple(sorted([nums[i]] + couple)))
        
        result = [list(i) for i in result]
        return result