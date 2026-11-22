class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def binpow(base, exp):
            res = 1
            while exp:
                if exp & 1:
                    res *= base
                base *= base
                exp >>= 1
            return res
        
        if n == 0: return float(1)
        if n < 0 : return 1.0/binpow(x, -n)
        return binpow(x, n)
