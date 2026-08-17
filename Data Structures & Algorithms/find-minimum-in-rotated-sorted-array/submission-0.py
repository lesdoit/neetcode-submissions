class Solution:
    def findMin(self, nums: List[int]) -> int:
        def check(idx):
            return 1 if nums[idx] < nums[0] else 0
        
        def bs():
            lo, hi = 0, len(nums)-1
            ans = 0
            while lo <= hi:
                mid = lo + (hi - lo)//2
                if check(mid):
                    ans = mid
                    hi = mid - 1
                else:
                    lo = mid + 1
            return nums[ans]
        
        return bs()
