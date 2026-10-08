class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        def rob_linear(houses: List[int]) -> int:
            m = len(houses)
            memo = [-1] * m

            def rec(idx: int) -> int:
                if idx >= m:
                    return 0
                if memo[idx] != -1:
                    return memo[idx]

                # Option 1: Rob current house and advance by 2
                rob_cur = houses[idx] + rec(idx + 2)
                # Option 2: Skip current house and advance by 1
                skip_cur = rec(idx + 1)

                memo[idx] = max(rob_cur, skip_cur)
                return memo[idx]

            return rec(0)

        # Case 1: Exclude the last house (indices 0 to n - 2)
        # Case 2: Exclude the first house (indices 1 to n - 1)
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))