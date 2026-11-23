class Solution:
    def isHappy(self, n: int) -> bool:
        
        def helper(num):
            ans = 0
            while num:
                ans += ((num%10) * (num%10))
                num //= 10
            return ans
        
        seen = set() 
        
        while n != 1:
            n = helper(n)
            
            if n in seen: return False
            seen.add(n)
        
        return True