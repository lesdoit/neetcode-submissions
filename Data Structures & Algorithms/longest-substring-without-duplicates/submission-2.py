class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # degenerate cases 
        if not s: 
            return 0
        
        # keep a window with l and r 
        # keep a hashmap of letter -> last index seen 
        # update the l ptr based on last seen index
        l, r = 0, 0
        ans = 1
        hm = {}
        while r < len(s): 
            if s[r] in hm:
                idx = hm[s[r]]
                # need to remove all the letters from prev l index to current l index.
                for i in range(l, idx + 1):
                    hm.pop(s[i])
                l = idx + 1
                hm[s[r]] = r
            else: 
                ans = max(ans, r - l + 1)
                hm[s[r]] = r
            r+=1 
        return ans 
