class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def rec(nums, n, cur, target, partial, res):
            # base case 
            if target == 0:
                res.append(partial)
                return
            elif cur == n:
                return
            elif target < 0: 
                return
            else: 
                # pick cur, see if remainder can summed using remaining nums
                # rec(nums, n, cur+1, target - nums[cur], partial + [nums[cur]], res)
                # pick cur, see if remainder can be summed using same list of nums 
                rec(nums, n, cur, target - nums[cur], partial + [nums[cur]], res)
                # do not pick cur number, and see if remainder can be summed 
                # using the remaining list of numbers 
                rec(nums, n, cur+1, target, list(partial), res)
                
        
        res = []
        rec(nums, len(nums), 0, target, [], res)
        return res