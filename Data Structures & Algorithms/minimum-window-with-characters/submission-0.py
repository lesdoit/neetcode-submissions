class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # degen case
        if len(t) > len(s): return ""
        
        # freq map of characters 
        countT = collections.Counter(t)
        # init an empty dict for freq map of characters in window
        countW = collections.defaultdict(int)

        res, resLen = "", float('inf')
        l, r = 0, 0
        have, need = 0, len(countT)
        while r < len(s): 
            if s[r] in countT: 
                countW[s[r]] += 1
                if countW[s[r]] == countT[s[r]]: 
                    have += 1
            while have == need: 
                if (r - l + 1) < resLen: 
                    res = s[l: r + 1]
                    resLen = len(res)
                if s[l] in countW: 
                    countW[s[l]] -= 1
                    if countW[s[l]] < countT[s[l]]: 
                        have -= 1
                l += 1
            r += 1

        return res