class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # check function
        # returns 1 if possible to eat all bananas within h for given value of k
        # 0 otherwise
        # this transforms the answer space into an array == 
        # lo = 0, hi = max(piles)
        # [0, 0, 0, 1] 
        def check(mid):
            total_time = 0
            for i in range(len(piles)):
                total_time += math.ceil(piles[i]/mid)
            return 1 if total_time <= h else 0
        
        def bs():
            lo, hi = 1, max(piles)
            ans = -1
            while lo <= hi:
                mid = lo + (hi - lo)//2
                if check(mid):
                    ans = mid 
                    hi = mid - 1
                else:
                    lo = mid + 1
            return ans
        
        return bs()

