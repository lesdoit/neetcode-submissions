class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # put all elements in a set 
        # check if smaller element of current number exists 
        # if it does, do not spawn a search 
        # only spawn a search if we are at the beginning of a seq
        if len(nums) == 0: 
            return 0
        n = set(nums)
        used = set()
        ans = 1
        for num in nums:
            if (num - 1 not in n) and (num not in used): 
                curr = 1
                while num + 1 in n:
                    num += 1
                    curr += 1
                used.add(num)
                ans = max(ans, curr)
        return ans

