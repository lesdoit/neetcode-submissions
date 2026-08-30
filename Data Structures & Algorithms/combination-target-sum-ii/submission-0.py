class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = sorted(candidates)
        
        def rec(nums, n, cur, target, partial, res):
            # base case 
            # print(f"cur: {cur}, target: {target}, part: {partial}")
            if target == 0:
                res.append(partial)
                return
            elif cur == n:
                return
            elif target < 0: 
                return
            else: 
                # pick cur, see if remaining list can sum upto target
                rec(nums, n, cur+1, target - nums[cur], partial + [nums[cur]], res)
                
                # skip current element and any other elements that have the same value 
                
                while cur + 1 < n and nums[cur] == nums[cur+1]: 
                    cur += 1
                rec(nums, n, cur+1, target, list(partial), res)
                
        
        res = []
        rec(nums, len(nums), 0, target, [], res)
        return res