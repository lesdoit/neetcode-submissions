class Solution:
    def getSum(self, a: int, b: int) -> int:
        # xor property - if bits are same -> 0
        # if bits are diff -> 1
        # carry 
        # due to the 2's complement representation of -ve numbers, we can directly use 
        # adder circuit to do subtraction as well. So, even if we perform just addition, we are good

        MAX_INT = 0x7FFFFFFF
        MASK = 0xFFFFFFFF
        ans = 0
        carry = 0
        for i in range(32):
            bit_mask = 1 << i
            first = 1 if a & bit_mask else 0
            second = 1 if b & bit_mask else 0
            xor_res = first ^ second
            bit = xor_res ^ carry
            carry = (first & second) | (carry & xor_res)

            ans = ans | (bit<<i)
        return ans if ans <= MAX_INT else ~(ans ^ MASK)