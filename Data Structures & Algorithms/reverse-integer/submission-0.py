class Solution:
    def reverse(self, x: int) -> int:
        # approach 1: use integer division and modulo (special handling for -ve nos)
        # approach 1.1: use int division with -ve digit accumulation 
        # approach 1.2: use positive digit accumulation and negate the answer later 
        # approach 2: use bit masks to clear sign bit and work on -ve numbers
        
        INT_MIN = -0x80000000
        INT_MAX = 0x7FFFFFFF 
        
        ans = 0
        num = x
        neg = False if num > -1 else True
        
        while num: 
            if neg:
                dig = 0
                if num % 10 != 0:
                    dig = (((num // 10) + 1) * 10) - num
                    num = (num // 10) + 1
                else: 
                    num = num // 10 
                if ans < -214748364 or (ans == -214748364 and dig > 8):
                    return 0
                ans *= 10 
                ans = ans + (-dig)
            else:
                dig = num%10
                if ans > 214748364 or (ans == 214748364 and dig > 8):
                    return 0
                ans *= 10
                ans += dig
                num = num//10
        return ans