class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        def rec(nums, cur, partial):
            # base case
            if cur == len(nums):
                res.append(partial.copy())
            else: 
                # pick current 
                rec(nums, cur + 1, partial + [nums[cur]])
                # do not pick current but also do not pick any next element that is same 
                # in value to the current element 
                while cur + 1 < len(nums) and nums[cur] == nums[cur+1]: 
                    cur+=1
                
                rec(nums, cur + 1, list(partial))
        
        rec(nums, 0, [])
        return res