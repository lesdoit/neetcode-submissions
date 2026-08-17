class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        ans = 0
        while lo <= hi:
            mid = lo + (hi - lo)//2
            if nums[mid] >= target:
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        
        return ans if nums[ans] == target else -1