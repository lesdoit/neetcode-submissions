class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def pivot_check(idx):
            return 1 if nums[idx] < nums[0] else 0
        
        def find_pivot_bs():
            lo, hi = 0, len(nums) - 1
            pivot_idx = 0
            while lo <= hi:
                mid = lo + (hi - lo)//2
                if pivot_check(mid):
                    pivot_idx = mid
                    hi = mid - 1
                else:
                    lo = mid + 1
            return pivot_idx
        
        def bs(lo, hi):
            ans = -1
            while lo <= hi:
                mid = lo + (hi - lo)//2
                if nums[mid] >= target:
                    ans = mid
                    hi = mid - 1
                else:
                    lo = mid + 1
            return ans if ans != -1 and nums[ans] == target else -1
        
        n = len(nums)
        pivot_idx = find_pivot_bs()
        # print(f"pivot_idx- {pivot_idx}")
        idx_right = bs(pivot_idx, n - 1) 
        idx_left = bs(0, pivot_idx - 1)

        return max(idx_left, idx_right)