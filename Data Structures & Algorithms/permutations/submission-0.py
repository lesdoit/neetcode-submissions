class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def rec(nums, visited, partial):
            # base case 
            if len(partial) == len(nums):
                res.append(partial.copy())
            else: 
                for i, num in enumerate(nums):
                    if not visited[i]:
                        visited[i] = True
                        partial.append(num)
                        rec(nums, visited, partial)
                        partial.pop()
                        visited[i] = False
        
        visited = [False for i in range(len(nums))]
        rec(nums, visited, [])
        return res