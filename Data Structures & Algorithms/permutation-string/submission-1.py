class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # degen case 
        if len(s2) < len(s1): return False 

        # freq map of chars of S1 
        countS1 = collections.Counter(s1)

        l, r = 0, len(s1) - 1
        countW = collections.Counter(s2[l:r])
        
        while r < len(s2):
            countW[s2[r]] += 1
            if countS1 == countW: 
                return True
            countW[s2[l]] -= 1
            l += 1
            r += 1
        
        return False
