class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # combinatorics 
        total_moves = (m - 1) + (n - 1)
        down_moves = m - 1

        def combinations(n: int, r: int) -> int:
            if r < 0 or r > n:
                return 0
            if r == 0 or r == n:
                return 1
            
            # Optimize by choosing the smaller r: C(n, r) == C(n, n - r)
            if r > n // 2:
                r = n - r

            res = 1
            for i in range(1, r + 1):
                # Multiply first, then integer divide by i
                # (res * (n - i + 1)) is mathematically guaranteed to be divisible by i
                res = (res * (n - i + 1)) // i
                
            return res
        if m == 0 and n == 0: return 0
        return combinations(total_moves, down_moves)