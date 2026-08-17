class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # sort the array first 
        # then start with two pointers and go 

        s= set(nums)
        ans, curr = 0, 1
        for num in nums:
            if num - 1 not in s: 
                while num + 1 in s:
                    num += 1
                    curr += 1
                ans = max(ans, curr)
                curr = 1
        return ans 

