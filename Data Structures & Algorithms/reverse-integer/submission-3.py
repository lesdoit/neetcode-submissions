class Solution:
    def reverse(self, x: int) -> int:
        ans = 0

        while x:
            q = int(x / 10)          # Truncates toward 0: -123 -> -12
            dig = x - q * 10         # Signed remainder:    -123 - (-120) = -3
            x = q

            if ans > 214748364 or (ans == 214748364 and dig > 7):
                return 0
            if ans < -214748364 or (ans == -214748364 and dig < -8):
                return 0

            ans = ans * 10 + dig

        return ans