class Solution:
    def reverse(self, x: int) -> int:
        if x == -2147483648:    # -2**31 would overflow INT_MAX when negated (and its
                                #reverse overflows anyway)
            return 0
        
        sign = -1 if x < 0 else 1
        x = abs(x)
        ans = 0
        while x:
            dig = x % 10
            if ans > 214748364 or (ans == 214748364 and dig > 7):
                return 0
            ans = ans * 10 + dig
            x //= 10
        return sign * ans