class Solution:
    def countBits(self, n: int) -> List[int]:
        # brian kernighan algo 
        res = [0] * (n+1)

        for i in range(n+1):
            cur = i 
            while cur != 0:
                # crux of algo. This clears the right most bit 1-bit 
                cur = cur & (cur - 1)
                res[i] += 1
        return res 