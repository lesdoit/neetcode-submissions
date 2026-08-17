class Solution:
    def twoSum(self, nums, start, end, target): 
        count = defaultdict(list)
        # O(n)
        for i in range(start, end):
            count[nums[i]].append(i)
        
        ans = []
        # O(n)
        for i in range(start, end):
            complement = target - nums[i]
            if complement in count: 
                for index in count[complement]:
                    if index != i:
                        ans.append([nums[i], nums[index]])
        return ans

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        n = len(nums)
        # fix a number and run two sum on the right side of the
        # list 
        for i in range(n):
            complement = 0 - nums[i]
            couples = self.twoSum(nums, i+1, n, complement)
            for couple in couples: 
                result.add(tuple(sorted([nums[i]] + couple)))
        
        result = [list(i) for i in result]
        return result