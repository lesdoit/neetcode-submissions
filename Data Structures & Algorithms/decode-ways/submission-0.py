class Solution:
    def numDecodings(self, s: str) -> int:
        # Total dp forms: knapsack, ends at i, multisequence, LR, game
        # Here, we need to partition an array using different cut points.
        # So, usually form 2 of dp which is "ends at i" is usually applicable

        # define dp (i) -> how many ways to decode a string that ends at i
        # transitions dp(i) = (dp(i-1) + 1) + (dp(i-2) + 1)
        # 1, 2, 2
        # ^
        # dp(0) = 1 if s[0] != 0 else 0/invalid

        # 1, 2 , 2 -> [[1,2], [12]]
        #    ^
        # dp(1) = 2

        # 1, 2, 2 -> [[1, 2, 2], [12, 2], [1, 22]]
        #       ^
        # dp(2) = 3

        # 1, 2, 2, 3 -> dp(2)  +  (dp(1) if s[i-1:i+1] is a valid decodable number else 0)
        n = len(s)
        memo = [-1] * n

        def valid_code(sliced):
            # print(f"check if sliced: {sliced} is a valid code")
            if sliced[0] == "0": return False
            num = int(sliced)
            return (1 <= num and num <= 26)

        def decode(i):
            if i == -1:
                return 1
            if memo[i] != -1:
                return memo[i]
            if i == 0:
                if "0" < s[i] and s[i] <= "9":
                    memo[i] = 1
                else:
                    memo[i] = 0
                return memo[i]

            ans = 0
            if valid_code(s[i:i+1]):
                print(f"i: {i}, i+1: {i+1}, s[i:i+1]: {s[i:i+1]} is a valid code")
                ans += decode(i - 1)
            if valid_code(s[i-1:i+1]):
                print(f"i-1: {i-1}, i+1: {i+1}, s[i-1:i+1]: {s[i-1:i+1]} is a valid code")
                ans += decode(i - 2)
            
            print(f"ans is {ans}")
            memo[i] = ans
            return memo[i]

        res = decode(n - 1)
        return res
