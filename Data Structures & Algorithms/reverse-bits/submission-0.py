class Solution:
    def reverseBits(self, n: int) -> int: 
        ans = 0
        num = n
        # accumulation formula = 2 * ans + 2^0(1) * bit
        for i in range(32):
            bit = (num>>i) & 1
            ans = (2*ans) + bit
        return ans