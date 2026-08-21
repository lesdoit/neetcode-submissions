class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def recurse(nums, n, curr, res, partial):
            # base case 
            if curr == n:
                res.append(partial)
            else: 
                # do not take curr element 
                recurse(nums, n, curr+1, res, list(partial))
                # take curr element 
                recurse(nums, n, curr+1, res, partial + [nums[curr]])
        
        res = [] 
        recurse(nums, len(nums), 0, res, [])
        return res


